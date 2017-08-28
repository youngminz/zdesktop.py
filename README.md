# zdesktop.py
ZDesktop Python Implementation

## Requirement
* python2.7 or python>=3.4
* `requests`. To install this library, type `pip install requests` at your terminal.

## Usage
```
$ python3 zdesktop.py
server ip and port: <ServerIP:Port>
username: <UserId>
password: <UserPw>

/api/login OK
/api/client/<UserId>/vms OK
/api/vm/<VmID>/start OK
/api/session/connect ERR (session.error.vm.state) retry after 10 seconds ..
/api/session/connect ERR (session.error.guesttool.not.running) retry after 10 seconds ..
/api/session/connect ERR (session.error.guesttool.not.running) retry after 10 seconds ..
/api/session/connect ERR (session.error.guesttool.not.running) retry after 10 seconds ..
/api/session/connect ERR (session.error.guesttool.not.running) retry after 10 seconds ..
/api/session/connect ERR (session.error.guesttool.not.running) retry after 10 seconds ..

ip address: <ServerIP>:<Port>
windows id: <WindowsID>
windows password: <WindowsPW>
```

## License
MIT License. For more information, see LICENSE.
