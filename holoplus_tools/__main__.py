from __future__ import annotations

import argparse
import logging

from .auth import get_auth_token
from .cookies import (
    COOKIES_FROM_BROWSER_HELP,
    COOKIES_FROM_BROWSER_METAVAR,
    extract_cookie_jar_from_browser,
)

_logger = logging.getLogger(__name__)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--get-auth-token", action="store_true")
    parser.add_argument(
        "--cookies-from-browser",
        required=True,
        metavar=COOKIES_FROM_BROWSER_METAVAR,
        help=COOKIES_FROM_BROWSER_HELP,
    )
    args = parser.parse_args()

    logging.basicConfig()
    _logger.setLevel(logging.INFO)

    if args.get_auth_token:
        _logger.info("Loading cookies")
        cookie_jar = extract_cookie_jar_from_browser(args.cookies_from_browser)

        _logger.info("Getting auth token. This will fail if you are not signed in browser.")
        token = get_auth_token(cookie_jar=cookie_jar)

        _logger.info("Token: %s", token)


if __name__ == "__main__":
    main()
