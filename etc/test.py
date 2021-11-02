from os import sys
from sys import path
import os, sys
import time
import hpe3parclient
import requests

# this is a hack to get the hpe driver module
# and it's utils module on the search path.
cmd_folder = os.path.realpath(os.path.abspath("..") )
if cmd_folder not in sys.path:
     sys.path.insert(0, cmd_folder)

requests.packages.urllib3.disable_warnings()

from hpe3parclient import client, exceptions
# from utils import *

username = "apiaccess"
password = "siesta3"

testVolName = "API-TEST-VOLUME"
testSNAPName = testVolName+"SNAP"
testCPGName = "TEST-CPG-NAME"

cl = client.HPE3ParClient("https://10.132.0.40:8080/api/v1")

cl.login("apiaccess", "siesta3")

#cl.createVolume(testVolName, testCPGName, 2048, "foo")

volumes = cl.getVolumes()
wsapi_version = cl.getWsApiVersion()
tasks = cl.getAllTasks()


print(volumes['members'][0]['name'])
print('------------------------------')
print(wsapi_version)
print(tasks['members'])

for t in tasks['members']:
    print(t)
    print('-------------------------------------------------------')
