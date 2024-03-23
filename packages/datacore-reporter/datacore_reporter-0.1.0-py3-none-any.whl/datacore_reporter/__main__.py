"""
Extract data easily from your Datacore controllers.
"""
import inspect
import logging
import os
import sys
from argparse import ArgumentParser, RawTextHelpFormatter
from contextlib import nullcontext
from types import FunctionType

from zut import OutTable, add_func_command, configure_logging, get_help_text

from . import __prog__, __version__, request
from .client import DatacoreClient

logger = logging.getLogger(__name__)

def main():
    configure_logging()
    OutTable.DEFAULT_EXCEL_ATEXIT = True
    
    datacore_names = DatacoreClient.get_configured_names()

    parser = ArgumentParser(prog=__prog__, description=get_help_text(__doc__), formatter_class=RawTextHelpFormatter, add_help=False, epilog='\n'.join(__doc__.splitlines()[2:]))
    
    group = parser.add_argument_group(title='General options')
    group.add_argument('-e', '--datacore', '--env', default=os.environ.get('DATACORE_DEFAULT_CLIENT'), help=f"Name of the Datacore API client to use. Available: {', '.join(datacore_names) if datacore_names else 'none'}.")
    group.add_argument('-h', '--help', action='help', help=f"Show this program help message and exit.")
    group.add_argument('--version', action='version', version=f"{__prog__} {__version__ or '?'}", help="Show version information and exit.")

    subparsers = parser.add_subparsers(title='Commands')
    add_func_command(subparsers, request.get)

    args = vars(parser.parse_args())
    handle = args.pop('handle', None)
    if not handle:
        logger.error(f"No command provided.")
        sys.exit(1)

    with get_datacore_context(handle, args):
        handle(**args)
        

def get_datacore_context(handle: FunctionType, args: dict):
    datacore_name = args.pop('datacore')
    need_datacore = 'datacore' in inspect.signature(handle).parameters

    if need_datacore:        
        if not datacore_name:
            datacore_names = DatacoreClient.get_configured_names()
            if len(datacore_names) > 1:
                logger.error(f"Name of the Datacore API client to use must be provided (option --datacore). Available: {', '.join(datacore_names) if datacore_names else 'none'}.")
                sys.exit(1)
            elif len(datacore_names) == 1:
                datacore_name = datacore_names[0]
            elif 'datacore' in args:
                logger.error(f"No Datacore API client configured.")
                sys.exit(1)
        
        context = DatacoreClient(datacore_name)
        args['datacore'] = context
    
    else:
        context = nullcontext()

    return context

if __name__ == '__main__':
    main()
