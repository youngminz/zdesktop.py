#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals

try:
    input = raw_input  # Python 2.7
except NameError:
    pass

import requests
import json
import time
try:
    from ConfigParser import ConfigParser  # Python 2.7
    config = ConfigParser()
    config.read("settings.ini")
    server = config.get("account", "server")
    login_id = config.get("account", "login_id")
    login_password = config.get("account", "login_password")

except:
    try:
        from configparser import ConfigParser  # Python 3
        config = ConfigParser()
        config.read("settings.ini")
        server = config["account"]["server"]
        login_id = config["account"]["login_id"]
        login_password = config["account"]["login_password"]

    except:
        server = input("server ip and port: ")
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

isPwd = False
try:
    for clientPreference in r.json()[0]["clientPreferences"]:
        if(isPwd and clientPreference["value"] != "true"):
            password = clientPreference["value"]
            vm_id = clientPreference["vmId"]
            break;
        if(clientPreference["value"] == "kau"):
            login = clientPreference["value"]
            client_id = clientPreference["clientId"]
            isPwd = True
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
