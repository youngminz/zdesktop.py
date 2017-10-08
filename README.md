# zdesktop.py
ZDesktop Python Implementation

## Requirement
* `python 2.7 or python>=3.4`
* `pip`
* `requests`

### Installation on macOS

1. Open Terminal.app
2. Type below commands
```bash
$ sudo easy_install pip
$ pip install requests
```

## Usage
```
$ python zdesktop.py
server ip and port: <Server IP:Port>
username: <User ID>
password: <User Password>

/api/login OK
/api/client/<UserId>/vms OK
/api/vm/<VmID>/start OK
/api/session/connect ERR (session.error.vm.state) retry after 10 seconds ..
/api/session/connect ERR (session.error.guesttool.not.running) retry after 10 seconds ..

ip address: <Server IP>:<Port>
windows id: <Windows ID>
windows password: <Windows Password>
```

## License
MIT License. For more information, see LICENSE.
