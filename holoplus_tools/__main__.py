# ruff: noqa: T201
from __future__ import annotations

import argparse
import logging

from .auth import auth_token, refresh_token
from .cookies import (
    COOKIES_FROM_BROWSER_HELP,
    COOKIES_FROM_BROWSER_METAVAR,
    extract_cookie_jar_from_browser,
)

_logger = logging.getLogger(__name__)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--auth-token", action="store_true")
    parser.add_argument("--refresh-token", default=None)
    parser.add_argument(
        "--cookies-from-browser",
        default="chrome",
        metavar=COOKIES_FROM_BROWSER_METAVAR,
        help=COOKIES_FROM_BROWSER_HELP,
    )
    args = parser.parse_args()

    logging.basicConfig()
    _logger.setLevel(logging.INFO)

    if args.auth_token:
        _logger.info("Loading cookies from %r", args.cookies_from_browser)
        cookie_jar = extract_cookie_jar_from_browser(args.cookies_from_browser)

        _logger.info("Getting auth token. This will fail if you are not signed in browser.")
        auth_response = auth_token(cookie_jar=cookie_jar)

        print(auth_response)

    if args.refresh_token:
        _logger.info("Refreshing token.")
        refresh_response = refresh_token(token=args.refresh_token)

        print(refresh_response)


if __name__ == "__main__":
    main()
