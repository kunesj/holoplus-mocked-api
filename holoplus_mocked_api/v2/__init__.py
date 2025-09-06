from __future__ import annotations

from typing import Annotated

import urllib.parse
import litestar
from litestar.response import Redirect
from litestar.params import Body, Parameter

from .models import AuthResponse, AuthTokenRequest, AuthTokenResponse


@litestar.get("/v2/auth", summary="/v2/auth")
async def v2__auth() -> AuthResponse:
    """
    Auth algorithm:
    - App calls this endpoint, gets "https://account.hololive.net/v1/ep/auth?****" url and opens it in browser
        that redirects to "https://account.hololive.net/v1/signin" for sign-in
    - Browser opens "https://api.holoplus.com/v2/auth/callback?code=***&state=***"
        that redirects back to app with "holoplus:///signup?state=***&code=***"
    - Finally app calls "https://api.holoplus.com/v2/auth/token" to get token
    """
    query = urllib.parse.urlencode(
        {
            "client_id": "H7HAzZpy8DnSDIoAohtafeU4pPBb1Ch9",
            "code_challenge": "**-****************************************",
            "code_challenge_method": "S256",
            "nonce": "*******************************************",
            "redirect_uri": "https://api.holoplus.com/v2/auth/callback",
            "response_type": "code",
            "scope": "openid+profile",
            "state": "********************************************",
        }
    )
    return AuthResponse(
        session_id="0000-000-0000000000000000000000000000000-00=",
        url=f"https://account.hololive.net/v1/ep/auth?{query}",
    )


@litestar.get("/v2/auth/callback", summary="/v2/auth/callback", status_code=302)
async def v2__auth__callback(
    *,
    code: Annotated[str, Parameter()],
    state_: Annotated[str, Parameter(query="state")],
) -> Redirect:
    query = urllib.parse.urlencode({"code": code, "state": state_})
    return Redirect(f"holoplus:///signup?{query}", status_code=302)


@litestar.post("/v2/auth/token", summary="/v2/auth/token", status_code=200)
async def v2__auth__token(
    data: Annotated[AuthTokenRequest, Body()],
) -> AuthTokenResponse:
    return AuthTokenResponse(token="JWT-TOKEN-PLACEHOLDER")


# FIXME: https://api.holoplus.com/v2/me/communities?limit=30
# FIXME: https://api.holoplus.com/v2/banners?filter_language=en
# FIXME: https://api.holoplus.com/v2/modules
# FIXME: https://api.holoplus.com/v2/groups/e9171551-cb2a-483e-8a77-fdffba8e632b
# FIXME: https://api.holoplus.com/v2/units/ebe86ce6-0013-46ff-b787-b1e49a6a1bcb


ROUTES: list[litestar.handlers.HTTPRouteHandler] = [
    v2__auth,
    v2__auth__callback,
    v2__auth__token,
]
