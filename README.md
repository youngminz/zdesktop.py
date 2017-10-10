# zdesktop.py
ZDesktop Python Implementation

## 요구 사항
* `python 2.7 or python>=3.4`
* `pip`
* `requests`

### macOS에서 설치하는 방법

1. 터미널 실행
2. 아래 명령어 실행
```bash
$ sudo easy_install pip
$ sudo pip install requests
```

## 사용법
1. `settings.ini`에 정보를 채움
2. 아래 명령어 실행
```bash
$ python zdesktop.py
/api/login OK
/api/client/<UserId>/vms OK
/api/vm/<VmID>/start OK
/api/session/connect ERR (session.error.vm.state) retry after 10 seconds ..
/api/session/connect ERR (session.error.guesttool.not.running) retry after 10 seconds ..

ip address: <Server IP>:<Port>
windows id: <Windows ID>
windows password: <Windows Password>
```

3. RDP 클라이언트 설치 후 2의 결과로 나온 접속 정보를 이용해 가상 PC에 접속
* Windows: 내장되어 있는 [원격 데스크톱 연결] 프로그램 사용
* macOS: [Mac App Store](https://itunes.apple.com/kr/app/microsoft-remote-desktop-8-0/id715768417?mt=12)
* Linux: remmina 등의 오픈 소스 사용
* Android: [Play Store](https://play.google.com/store/apps/details?id=com.microsoft.rdc.android&hl=ko)
* iOS: [App Store](https://itunes.apple.com/kr/app/microsoft-remote-desktop/id714464092?mt=8)

## License
MIT License. For more information, see LICENSE.
