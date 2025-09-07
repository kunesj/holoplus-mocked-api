# Holoplus Mocked API

Mock version of the api.holoplus.com API. Currently incomplete, and might become outdated in the future.

The main purpose of this project is to document the API, to make it easier to develop apps that need to access it.
It should also be useful for tests.


## Quick Setup

Install:

- Use Python 3.11+
- Install dependencies `pip install -r requirements.txt -c constraints.txt`

Run:

```shell
litestar --app holoplus_mocked_api.app:create_app run --port 8080
```

Generated documentation can be found at http://127.0.0.1:8080/schema.


## Headers

Most requests are sent with following headers

```
accept-encoding: gzip
accept-language: en
app-version: 3.0.0 (194)
authorization: Bearer **********
content-type: text/plain; charset=utf-8
device-id: 01234b988c2b9c52
device-name: emu64xa (google)
host: api.holoplus.com
os-version: 16
release-type: app_data
user-agent: Dart/3.7 (dart:io)
```


## Development

- Use pre-commit

### Inspecting Holoplus requests

- Install [Android Studio](https://developer.android.com/studio)
- Install [HTTP Toolkit](https://httptoolkit.com/)
- Install `adb` (`sudo apt install adb` on Ubuntu)
- [Create](https://developer.android.com/studio/run/managing-avds) new virtual device in Android Studio and make sure to select "Google APIs" services (Google Play must not be installed)
- Start the emulator, and enable root with `adb root`
- [Download Holoplus XAPK](https://apkpure.com/holoplus/com.cover_corp.holoplus), open it as archive and extract `*.apk` files
- Install Holoplus with `adb install-multiple -r "com.cover_corp.holoplus.apk" "config.arm64_v8a.apk" "config.en.apk" "config.fr.apk" "config.mdpi.apk"`
- Open HTTP Toolkit and select to connect to Android over adb. Follow instructions on screen. Everything should be green.
- Open Holoplus app and do something, the requests should be visible in HTTP Toolkit.
