from __future__ import annotations

import logging
import urllib.parse
from typing import TypedDict

import requests
import requests.cookies

_logger = logging.getLogger(__name__)


class HoloplusAuthError(requests.HTTPError):
    pass


class HoloplusToken(TypedDict):
    id_token: str
    refresh_token: str
    expires_in: int
    is_new_user: bool


def get_auth_token(
    *,
    cookie_jar: requests.cookies.RequestsCookieJar,
    # This key should be static and same for everyone (I think)
    holoplus_google_key: str = "AIzaSyBIBy1CboBwrCShfY1CixfRRynJRF06vx0",
) -> HoloplusToken:
    # 1. `https://api.holoplus.com/v2/auth` -> `https://account.hololive.net/v1/ep/auth?***`

    api_auth_url = "https://api.holoplus.com/v2/auth"

    response = requests.request("GET", api_auth_url, timeout=30)
    if not response.ok:
        _logger.error("Response: %s", response.content)
    response.raise_for_status()

    data = response.json()
    session_id = data["session_id"]
    account_auth_url = data["url"]

    if not account_auth_url.startswith("https://account.hololive.net/v1/ep/auth?"):
        raise HoloplusAuthError("Unexpected auth url", api_auth_url, account_auth_url)

    # 2. `https://account.hololive.net/v1/ep/auth?***` -> `https://api.holoplus.com/v2/auth/callback?***`
    # - done in browser
    # - redirects to `https://api.holoplus.com/v2/auth/callback?***` if already signed in
    # - redirects to `https://account.hololive.net/v1/signin` if not signed in

    with requests.Session() as session:
        session.cookies = cookie_jar

        response = session.request(method="GET", url=account_auth_url, timeout=30, allow_redirects=False)
        api_callback_url = response.headers.get("Location")

        if response.status_code != 302:
            raise HoloplusAuthError("Unexpected auth status code", account_auth_url, response.status_code)

        if api_callback_url == "https://account.hololive.net/v1/signin":
            raise HoloplusAuthError(
                "Not signed in! Sign in at https://account.hololive.net/v1/signin and try again.",
                account_auth_url,
                api_callback_url,
            )

        if not api_callback_url or not api_callback_url.startswith("https://api.holoplus.com/v2/auth/callback?"):
            raise HoloplusAuthError("Unexpected auth redirect", account_auth_url, api_callback_url)

        # 3. `https://api.holoplus.com/v2/auth/callback?***` -> `holoplus://****`
        # - this is done in browser via redirect

        response = session.request(method="GET", url=api_callback_url, timeout=30, allow_redirects=False)
        holoplus_url = response.headers.get("Location")

        if response.status_code != 302:
            raise HoloplusAuthError("Unexpected auth status code", api_callback_url, response.status_code)

        if not holoplus_url or not holoplus_url.startswith("holoplus://"):
            raise HoloplusAuthError("Unexpected auth redirect", api_callback_url, holoplus_url)

    # 4. `holoplus://****` -> `https://api.holoplus.com/v2/auth/token?***`
    # - this should give us Firebase token
    # - the state and code from holoplus url must be used without decoding them

    url_parsed = urllib.parse.urlparse(holoplus_url)
    if url_parsed.path != "/signup":
        raise HoloplusAuthError("Unexpected holoplus:// path", holoplus_url)

    query_encoded = {}
    for part in url_parsed.query.split("&"):
        name, value = part.split("=", maxsplit=1)
        query_encoded[name] = value

    response = requests.request(
        "POST",
        "https://api.holoplus.com/v2/auth/token",
        json={
            "session_id": session_id,
            "code": query_encoded["code"],
            "state": query_encoded["state"],
        },
        timeout=30,
    )
    if not response.ok:
        _logger.error("Response: %s", response.content)
    response.raise_for_status()

    data = response.json()
    firebase_token = data["token"]

    # 5. `https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyCustomToken?***`
    # - this should convert Firebase token to Holoplus tokens

    response = requests.request(
        "POST",
        "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyCustomToken",
        params={
            "key": holoplus_google_key,
        },
        json={
            "token": firebase_token,
            "returnSecureToken": True,
        },
        timeout=30,
    )
    if not response.ok:
        _logger.error("Response: %s", response.content)
    response.raise_for_status()

    data = response.json()
    return HoloplusToken(
        id_token=data["idToken"],
        refresh_token=data["refreshToken"],
        expires_in=int(data["expiresIn"]),
        is_new_user=data["isNewUser"],
    )
