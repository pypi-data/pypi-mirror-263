"""
Make custom requests on the Datacore API.
"""
from argparse import ArgumentParser
import json
from pprint import pformat
import sys
from zut import Literal, out_file, ExtendedJSONEncoder
from .client import DatacoreClient


def get(datacore: DatacoreClient, endpoint: str, api_version: str = None, out: str = None, fmt: Literal['json','pprint'] = None):
    """
    Make a custom GET request on the Datacore API.
    """
    result = datacore.get_with_retries(endpoint, api_version=api_version)
    with out_file(out, title=endpoint) as o:
        if fmt == 'pprint' or (fmt is None and (o.out == sys.stdout or o.out == sys.stderr)): #TODO: dir=DEFAULT_OUT_DIR_MASK (if relative)
            print(pformat(result, sort_dicts=False), file=o.file)
        else:
            json.dump(result, fp=o.file, indent=4, cls=ExtendedJSONEncoder, ensure_ascii=False)

def _add_arguments(parser: ArgumentParser):
    parser.add_argument('endpoint', help="API endpoint (example: /hosts).")
    parser.add_argument('--api-version', default=None, help="Use a specific API version (example: 2.0).")
    parser.add_argument('-o', '--out', help="Output JSON file (default: stdout).")
    parser.add_argument('--pprint', action='store_const', const='pprint', dest='fmt', help="Force pprint format.")
    parser.add_argument('--json', action='store_const', const='json', dest='fmt', help="Force JSON format.")

get.add_arguments = _add_arguments
