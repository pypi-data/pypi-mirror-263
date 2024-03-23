"""CLI for 'GPDT' package.

# Autocompletion

https://click.palletsprojects.com/en/8.1.x/shell-completion/

_GPDT_COMPLETE=bash_source gpdt > ~/.gpdt-complete.bash

. ~/.gpdt-complete.bash

"""

# ==============================================================
# Implementation of 1st ports interface for CLI 
# ==============================================================
import sys
import os
ACTIVE_WINGDEBUG = os.environ.get('ACTIVE_WINGDEBUG', 'False').lower()
    
if ACTIVE_WINGDEBUG in ('true', 'yes', '1'):
    try:
        # print(f"Trying to connect to a remote debugger..")
        sys.path.append(os.path.dirname(__file__))
        from . import wingdbstub
    except Exception as why:
        print(f"{why}")
        print("Remote debugging is not found or configured: Use ACTIVE_WINGDEBUG=True to activate")
else:
    # print("Remote debugging is not selected") # don't show: problem with bash_source autocompletion
    pass


# ---------------------------------------------------------
# local imports
# ---------------------------------------------------------
from ..helpers.loaders import ModuleLoader

# -----------------------------------------------
# import main cli interface (root)
# -----------------------------------------------

from .main import main

# ---------------------------------------------------------
# Load active port (click) modules
# from `config.yaml` config file 
# ---------------------------------------------------------

loader = ModuleLoader(__file__)    
names = loader.available_modules()
ACTIVE_PORTS = loader.load_modules(names)

#openapi_tags = []
#for port in ACTIVE_PORTS:
    #if hasattr(port, "TAG"):
        #openapi_tags.append({
            #"name": port.TAG, 
            #"description": port.DESCRIPTION, 
            #"order": port.API_ORDER, 
        #})

#ACTIVE_PORTS.sort(key=lambda x: getattr(x, "API_ORDER", 1000), reverse=True)


#from .config import config
#from .setup import setup
#from .workspace import workspace

# -----------------------------------------------
# import other project submodules/subcommands
# -----------------------------------------------

#from .publish import publish

# from .plan import plan
# from .real import real
# from .roles import role
# from .run import run
# from .target import target
# from .test import test
# from .users import user
# from .watch import watch
