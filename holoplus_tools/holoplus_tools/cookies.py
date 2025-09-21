from __future__ import annotations

import logging
import re

import requests.cookies
import yt_dlp.cookies

_logger = logging.getLogger(__name__)
COOKIES_FROM_BROWSER_METAVAR = "BROWSER[+KEYRING][:PROFILE][::CONTAINER]"
COOKIES_FROM_BROWSER_HELP = (
    "The name of the browser to load cookies from. "
    f"Currently supported browsers are: {', '.join(sorted(yt_dlp.cookies.SUPPORTED_BROWSERS))}. "
    "Optionally, the KEYRING used for decrypting Chromium cookies on Linux, "
    "the name/path of the PROFILE to load cookies from, "
    'and the CONTAINER name (if Firefox) ("none" for no container) '
    "can be given with their respective separators. "
    "By default, all containers of the most recently accessed profile are used. "
    f"Currently supported keyrings are: {', '.join(map(str.lower, sorted(yt_dlp.cookies.SUPPORTED_KEYRINGS)))}"
)


class PatchedYDLLogger(yt_dlp.cookies.YDLLogger):
    def __init__(self, ydl: yt_dlp.YoutubeDL | None = None) -> None:
        super().__init__(ydl=ydl)
        self._done: set[str] = set()

    def debug(self, message: str) -> None:
        _logger.debug(message)

    def info(self, message: str) -> None:
        _logger.info(message)

    def warning(self, message: str, only_once: bool = False) -> None:
        if only_once and message in self._done:
            return

        _logger.warning(message)

        if only_once:
            self._done.add(message)

    def error(self, message: str, *, is_error: bool = True) -> None:
        _logger.error(message)

    def stdout(self, message: str) -> None:
        _logger.info(message)

    def stderr(self, message: str) -> None:
        _logger.error(message)


def extract_cookie_jar_from_browser(cookies_from_browser: str) -> requests.cookies.RequestsCookieJar:
    browser_name, profile, keyring, container = parse_cookies_from_browser_arg(cookies_from_browser)
    yt_dlp_cookie_jar: yt_dlp.cookies.YoutubeDLCookieJar = yt_dlp.cookies.extract_cookies_from_browser(
        browser_name=browser_name, profile=profile, logger=PatchedYDLLogger(), keyring=keyring, container=container
    )

    cookie_jar = requests.cookies.RequestsCookieJar()
    cookie_jar.update(yt_dlp_cookie_jar)

    return cookie_jar


def parse_cookies_from_browser_arg(cookies_from_browser: str) -> tuple[str, str | None, str | None, str | None]:
    """
    Parses cookies_from_browser argument.
    Borrowed from yt-dlp.
    """
    container = None

    mobj = re.fullmatch(
        r"""(?x)
        (?P<name>[^+:]+)
        (?:\s*\+\s*(?P<keyring>[^:]+))?
        (?:\s*:\s*(?!:)(?P<profile>.+?))?
        (?:\s*::\s*(?P<container>.+))?
    """,
        cookies_from_browser,
    )
    if mobj is None:
        raise ValueError(f"invalid cookies from browser arguments: {cookies_from_browser}")

    browser_name, keyring, profile, container = mobj.group("name", "keyring", "profile", "container")
    browser_name = browser_name.lower()
    if browser_name not in yt_dlp.cookies.SUPPORTED_BROWSERS:
        raise ValueError(
            f'unsupported browser specified for cookies: "{browser_name}". '
            f"Supported browsers are: {', '.join(sorted(yt_dlp.cookies.SUPPORTED_BROWSERS))}"
        )

    if keyring is not None:
        keyring = keyring.upper()
        if keyring not in yt_dlp.cookies.SUPPORTED_KEYRINGS:
            raise ValueError(
                f'unsupported keyring specified for cookies: "{keyring}". '
                f"Supported keyrings are: {', '.join(sorted(yt_dlp.cookies.SUPPORTED_KEYRINGS))}"
            )

    return browser_name, profile, keyring, container
