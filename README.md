# Holoplus Mocked API

Experimental mock version of the api.holoplus.com API. Might be incomplete or outdated.

The main purpose of this project is document the API to make it easier to develop apps that need access to access Holoplus API.
It should also be useful for tests.


## Start

```shell
litestar --app holoplus_mocked_api.app:create_app run --port 8080
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
