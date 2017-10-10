#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals

try:
    input = raw_input
except NameError:
    pass

import requests
import json
import time

server = input("server ip and port: ")  # Example: 123.123.123.123:1234
login_id = input("username: ")
login_password = input("password: ")

print()

r = requests.post("http://{}/api/login".format(server),
                  headers={"User-Agent": "ZDCLIENT", "Cache-Control": "no-cache"},
                  data={"username": login_id, "password": login_password})

if r.status_code == 200:
    print("/api/login OK")
else:
    print("/api/login ERR")
    exit(1)
    
token = r.json()["message"]

r = requests.get("http://{}/api/client/{}/vms".format(server, login_id),
                 headers={"User-Agent": "ZDCLIENT", "Content-Type": "plain/text"},
                 params={"token": token})

try:
    login = r.json()[0]["clientPreferences"][1]["value"]
    password = r.json()[0]["clientPreferences"][0]["value"]

    client_id = r.json()[0]["clientPreferences"][0]["clientId"]
    vm_id = r.json()[0]["clientPreferences"][0]["vmId"]

    service_host_id = r.json()[0]["serviceHostId"]
    
    print("/api/client/{}/vms OK".format(login_id))
except:
    print("/api/client/{}/vms ERR".format(login_id))
    exit(1)

r = requests.post("http://{}/api/vm/{}/start".format(server, vm_id),
                  headers={"User-Agent": "ZDCLIENT", "Content-Type": "application/json"},
                  params={"token": token, "endPointId": str(service_host_id)}, data="{}")

if r.status_code == 200:
    print("/api/vm/{}/start OK".format(vm_id))
else:
    print("/api/vm/{}/start ERR".format(vm_id))
    exit(1)

while True:
    r = requests.post("http://{}/api/session/connect".format(server),
                      headers={"User-Agent": "ZDCLIENT", "Content-Type": "application/json", "Cache-Control": "no-cache"},
                      params={"token": token},
                      data=json.dumps({"clientId": client_id, "vmId": vm_id, "type": "RDP"}, separators=(',', ':')))

    if r.status_code != 200:
        print("/api/session/connect ERR ({}) retry after 10 seconds ..".format(r.json()["message"]))
        time.sleep(10)
    else:
        break

print()

print("ip address: {}:{}".format(r.json()["ip"], r.json()["port"]))
print("windows id: {}".format(login))
print("windows password: {}".format(password))
