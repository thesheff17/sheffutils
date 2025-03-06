#!/usr/bin/env python3

import os
import sys
from datetime import datetime


# this block help manages 3rd party imports
# you can still use all the code that doesn't 
# depend on 3rd party modules but you can also
# build off requirements.txt to build a virtualenv
# to fix this message. I only want to manage 1 utils file.
try:
    import boto
    import boto3
    import requests
    import flask
except ModuleNotFoundError as f:
    print ({f})
    print ("pip module(s) not found.  Exiting script.")
    print ("Please read README.md to create virtualenv.")
    sys.exit(1)
except Exception as e:
    print ("something else went wrong...")
    sys.exit(1)

######################################
#                                    #
# basic def to manage terminal stuff #
# namespace: terminal_               #
#                                    #
######################################
def terminal_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

######################################
#                                    #
# basic def to random things I need  #
#                                    #
######################################
def get_timestamp():
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d-%H-%M-%S-%f")
    return formatted_date

def hello_world():
    print ("hello world")
    print (f"timestamp: {get_timestamp()}")
    print (f"python version: {sys.version}")
    return "hello world"
