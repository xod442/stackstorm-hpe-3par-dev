from os import sys
from sys import path
import os, sys
import time
import hpe3parclient

# this is a hack to get the hpe driver module
# and it's utils module on the search path.
cmd_folder = os.path.realpath(os.path.abspath("..") )
if cmd_folder not in sys.path:
     sys.path.insert(0, cmd_folder)

from hpe3parclient import client, exceptions
from utils import *

username = "admin"
password = "hpe"

testVolName = "API-TEST-VOLUME"
testSNAPName = testVolName+"SNAP"
testCPGName = "TEST-CPG-NAME"

cl = client.HPE3ParClient("https://10.10.22.241:8080/api/v1")

# Create Volume Name
try:
    cl.createVolume(testVolName, testCPGName, 1000)
except exceptions.HTTPUnauthorized as ex:
    print("You must login")
except Exception as ex:
    print(ex)
