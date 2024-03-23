from __future__ import annotations

import inspect
import logging
import os
import re
from collections.abc import Callable, Iterator
from configparser import _UNSET
from pathlib import Path
from time import sleep
from typing import Any, Literal, TypeVar, overload
from uuid import UUID

from zut import Filters, JSONApiClient, get_config, resolve_host

import datacore_reporter

from . import __prog__


class DatacoreClient(JSONApiClient):
    """
    Main entry point of the library: make requests to Datacore API.
    """
    def __init__(self, name: str = None, *, host: str = None, controller: str = None, user: str = None, password: str = None, no_ssl: bool = None):
        """
        Create a new Datacore API client.

        If `host`, `user`, `password` or `no_ssl_verify` options are not provided, they are read from configuration file
        in section `[datacore-reporter]` (or `[datacore-reporter:{name}]` if `name` is given).

        :param name: An optional name to distinguish between several Datacore contexts.
        :param host: Host name of the Datacore server exposing the API (may be an admin console or a Datacore controller).
        :param controller: Host name of the actual Datacore controller to use, if `host` is an admin console.
        :param user: Name of the vCenter user having access to the API.
        :param password: Password of the vCenter user having access to the API.
        """
        self.name = name or 'default'
        
        config = get_config(datacore_reporter)
        section = __prog__ if self.name == 'default' else f'{__prog__}:{self.name}'
            
        self.host = host if host is not None else config.get(section, 'host')
        self.controller = controller if controller is not None else config.get(section, 'controller', fallback=None)
        self.user = user if user is not None else config.get(section, 'user')
        self.password = password if password is not None else config.get(section, 'password')
        self.no_ssl = no_ssl if no_ssl is not None else config.getboolean(section, 'no_ssl', fallback=False)
        
        self.logger = logging.getLogger(f'{self.__class__.__module__}.{self.__class__.__qualname__}.{self.name}')

        self.nonversionned_base_url = f"http{'' if self.no_ssl else 's'}://{self.host}/RestService/rest.svc"
        self.base_url = f'{self.nonversionned_base_url}/1.0'

        self._retry_succeeded = False
        self._cached_objs: dict[str,dict[str]] = {}
        self._cached_perfs: dict[str,dict[str]] = {}


    #region Authentication

    def get_request_headers(self, url: str):
        if not hasattr(self, '_headers'):
            host_addrs = resolve_host(self.host, timeout=2.0)
            if not host_addrs:
                raise ValueError(f"Cannot resolve host name \"{self.host}\"")
            
            host_addr = host_addrs[0]
            self.logger.info(f'Connect to datacore API endpoint {host_addr} ({self.host}) with user {self.user}')

            self._headers = super().get_request_headers(url)
            self._headers['ServerHost'] = self.controller
            self._headers['Authorization'] = f'Basic {self.user} {self.password}'
        
        return self._headers

    #endregion


    #region Retrieve objects

    def get_with_retries(self, endpoint: str, *, params: dict = None, api_version: str = None, retries = 5):
        """
        Necessary because datacore API returns empty data the first time it is run.
        """
        if api_version:
            url = self.prepare_url(endpoint, params=params, base_url=f"{self.nonversionned_base_url}/{api_version}")
        else:
            url = self.prepare_url(endpoint, params=params)

        response = self.get(url, params=params)
        if response or self._retry_succeeded:
            return response
         
        while retries > 0:
            self.logger.info(f'Waiting for data ({retries} retries remaining)')
            sleep(1)

            response = self.get(url, params=params)
            if response:
                self._retry_succeeded = True
                return response
            
            retries -= 1

        raise ValueError('Max retries reached')


    def get_obj(self, endpoint: str, id: str, default = _UNSET, *, prop: str|None = None, api_version: str = None):
        if not id:        
            if default is _UNSET:
                raise KeyError(f"Requested empty id for endpoint {endpoint}")
            return default
        
        objs = self.get_objs_by_id(endpoint, api_version=api_version)

        lower_id = id.lower()
        if lower_id in objs:
            obj = objs[lower_id]
            if prop is not None:
                return obj[prop]
            return obj
        else:
            if default is _UNSET:
                raise KeyError(f"Id {id} not found in endpoint {endpoint}")
            return default
        

    def get_objs_by_id(self, endpoint: str, reset_cache = False, api_version: str = None) -> dict[str,dict[str,Any]]:
        cachename = endpoint + (f'-{api_version}' if api_version else '')

        if reset_cache or not cachename in self._cached_objs:
            response = self.get_with_retries(endpoint, api_version=api_version)

            self._cached_objs[cachename] = {}
            for obj in response:
                self._cached_objs[cachename][obj["Id"].lower()] = obj

        return self._cached_objs[cachename]

    #endregion


    #region Retrieve performance data

    def get_perf(self, perftype: str, id: str, default = _UNSET, *, prop: str|None = None):
        if not id:        
            if default is _UNSET:
                raise KeyError(f"Requested empty id for endpoint {perftype}")
            return default

        perfs = self.get_perfs_by_id(perftype)

        lower_id = id.lower()
        if lower_id in perfs:
            obj = perfs[lower_id]
            if prop is not None:
                return obj[prop]
            return obj
        else:
            if default is _UNSET:
                raise KeyError(f"Id {id} not found in endpoint {perftype}")
            return default
        

    def get_perfs_by_id(self, perftype: str, reset_cache = False) -> dict[str,dict[str,Any]]:
        """
        Retrieve performance data.
        
        See: https://docs.datacore.com/RESTSupport-WebHelp/RESTSupport-WebHelp/Getting_Performance_Statistcs.htm
        """     
        if reset_cache or not perftype in self._cached_perfs or not self._cached_perfs[perftype]:                
            results = self.get(f'performancebytype/{perftype}')

            if not results:
                self.logger.info(f"Wait for 2.5 seconds to retrieve {perftype}")
                sleep(2.5)
                results = self.get(f'performancebytype/{perftype}')

                if not results:
                    raise ValueError(f"Could not retrieve {perftype}")
            
            self._cached_perfs[perftype] = {}
            for result in results:
                self._cached_perfs[perftype][result['ObjectId'].lower()] = result['PerformanceData']

        return self._cached_perfs[perftype]
        

    def init_perfs(self, *perftypes: str):
        """
        Initialize performance data counters.
        
        See: https://docs.datacore.com/RESTSupport-WebHelp/RESTSupport-WebHelp/Getting_Performance_Statistcs.htm
        """
        if not perftypes:
            raise ValueError(f"At least one enpoint must be provided")
        
        for perftype in perftypes:
            self.get(f'performancebytype/{perftype}')

    #endregion


    #region Instance helpers

    DEFAULT_OUT_DIR_MASK = Path('data/datacore-{datacore}')

    def compile_path_mask(self, path: os.PathLike, *, parent_mkdir = False, mkdir = False, **attrs):
        path = Path(str(path).format(datacore=self.name, **attrs))
        if mkdir:
            path.mkdir(parents=True, exist_ok=True)
        elif parent_mkdir:
            path.parent.mkdir(parents=True, exist_ok=True)
        return path

    #endregion


    #region Class helpers

    @classmethod
    def get_configured_names(cls) -> list[str]:
        try:
            return cls._configured_names
        except AttributeError:
            pass

        cls._configured_names = []

        config = get_config(datacore_reporter)    
        for section in config.sections():
            if m := re.match(r'^' + re.escape(__prog__) + r'(?:\:(.+))?', section):
                name = m[1]
                if name == 'default':
                    raise ValueError(f"Invalid configuration section \"{section}\": name \"default\" is reserved")
                if not name:
                    name = 'default'
                if not name in cls._configured_names:
                    cls._configured_names.append(name)

        return cls._configured_names
    
    #endregion
