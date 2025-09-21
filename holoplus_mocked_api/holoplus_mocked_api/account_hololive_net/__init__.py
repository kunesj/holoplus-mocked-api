from __future__ import annotations

from typing import Annotated, Any

import urllib.parse

import litestar
from litestar import status_codes, Request
from litestar.types import ControllerRouterHandler
from litestar.response import Redirect, Response
from litestar.params import Body, Parameter
from litestar.openapi.spec import Example


@litestar.get(
    "/account.hololive.net/v1/ep/auth",
    summary="/account.hololive.net/v1/ep/auth",
    status_code=status_codes.HTTP_302_FOUND,
)
async def v1_ep_auth(
    request: Request[Any, Any, Any],
    *,
    client_id: Annotated[str, Parameter(examples=[Example(value="H7HAzZpy8DnSDIoAohtafeU4pPBb1Ch9")])],
    code_challenge: Annotated[str, Parameter(examples=[Example(value="nL-CnJSXngQBv0xW7Zgb1Xut8jBhtbfAPCEcAh86oRU")])],
    code_challenge_method: Annotated[str, Parameter(examples=[Example(value="S256")])],
    nonce: Annotated[str, Parameter(examples=[Example(value="KhcI74qcBR3KavUiWbts-qKU58A3uopAonE0JXrmBnU")])],
    redirect_uri: Annotated[str, Parameter(examples=[Example(value="https://api.holoplus.com/v2/auth/callback")])],
    response_type: Annotated[str, Parameter(examples=[Example(value="code")])],
    scope: Annotated[str, Parameter(examples=[Example(value="openid+profile")])],
    state_: Annotated[
        str, Parameter(query="state", examples=[Example(value="kMRJ2iYeaDYYDlJj13Azse6_GGbyZr1ZC5x5UvrfmIM=")])
    ] = "",
) -> Redirect:
    """
    - Redirects to "https://api.holoplus.com/v2/auth/callback" if signed in
    - Redirects to "https://account.hololive.net/v1/signin" if not signed in
    """
    if redirect_uri == "https://api.holoplus.com/v2/auth/callback":
        redirect_uri = "/api.holoplus.com/v2/auth/callback"

    # TODO: detect what user is signed in
    logged_in = True

    if logged_in:
        query = urllib.parse.urlencode({"code": "some-auth-code", "state": state_})
        url = f"{redirect_uri}?{query}"
    else:
        url = "/account.hololive.net/v1/signin"

    return Redirect(url, status_code=status_codes.HTTP_302_FOUND)


@litestar.get(
    "/account.hololive.net/v1/signin",
    summary="/account.hololive.net/v1/signin",
    media_type=litestar.MediaType.HTML,
)
async def v1_signin() -> Response:
    """Returns hololive signin page"""
    return litestar.Response(
        media_type=litestar.MediaType.HTML,
        # TODO: implement actual sign in page
        #   Successful sign in should redirect to /account.hololive.net/v1/auth/google/callback
        content="<h1>Sign in page</h1>",
    )


@litestar.get(
    "/account.hololive.net/v1/auth/google/callback",
    summary="/account.hololive.net/v1/auth/google/callback",
    status_code=status_codes.HTTP_302_FOUND,
)
async def v1_auth_google_callback(
    request: Request[Any, Any, Any],
    *,
    state_: Annotated[
        str,
        Parameter(
            query="state",
            examples=[
                Example(
                    value="5lYionNCuqGUzZb5yrRPuKvbjgxIn_0jh2EqgyRip7Bio64NN6rNJNha6w0Zm2bUER4ugfNFSeXm4l4fV7BiwQ=="
                )
            ],
        ),
    ],
    code: Annotated[
        str,
        Parameter(
            examples=[Example(value="4/0AVMBsJhiNuOZuLhyiNj8rT4EhKqLd2dofHUu_XoMSZU16p6moDAxwKnK61i5l9MuzzoSxg")]
        ),
    ],
    scope: Annotated[
        str,
        Parameter(
            examples=[
                Example(
                    value="email+profile+https://www.googleapis.com/auth/userinfo.profile+https://www.googleapis.com/auth/userinfo.email+openid"
                )
            ]
        ),
    ],
    authuser: Annotated[str, Parameter(examples=[Example(value="0")])],
    prompt: Annotated[str, Parameter(examples=[Example(value="consent")])],
) -> Redirect:
    """
    If successful, redirects to the original `/v1/ep/auth/**` url that started the signin process.
    """
    # TODO: replace placeholder values with real ones from storage
    query = urllib.parse.urlencode(
        {
            "client_id": "???",
            "code_challenge": "???",
            "code_challenge_method": "S256",
            "nonce": "???",
            "redirect_uri": "/api.holoplus.com/v2/auth/callback",
            "response_type": "code",
            "scope": "openid+profile",
            "state": "???",
        }
    )
    url = f"/v1/ep/auth?{query}"

    return Redirect(url, status_code=status_codes.HTTP_302_FOUND)


ROUTES: list[ControllerRouterHandler] = [
    litestar.Router(
        "",
        tags=["account.hololive.net"],
        route_handlers=[
            v1_ep_auth,
            v1_signin,
            v1_auth_google_callback,
        ],
    ),
]
