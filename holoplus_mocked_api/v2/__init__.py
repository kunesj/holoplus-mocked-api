from __future__ import annotations

import uuid
from typing import Annotated

import urllib.parse
import litestar
from litestar.exceptions import NotFoundException
from litestar.response import Redirect
from litestar.params import Body, Parameter
from litestar.openapi.spec import Example

from .models import (
    AuthResponse,
    AuthTokenRequest,
    AuthTokenResponse,
    V2CommunityItem,
    V2CommunitiesResponse,
    BannersResponse,
    ModulesResponse,
    Group,
    Unit,
)
from .data import COMMUNITIES_MAP, BANNERS_MAP, MODULES_MAP, GROUPS_MAP, UNITS_MAP


@litestar.get("/v2/auth", summary="/v2/auth")
async def v2__auth() -> AuthResponse:
    """
    Auth algorithm:
    - App calls this endpoint, gets "https://account.hololive.net/v1/ep/auth?****" url and opens it in browser
        that redirects to "https://account.hololive.net/v1/signin" for sign-in
    - Browser opens "https://api.holoplus.com/v2/auth/callback?code=***&state=***"
        that redirects back to app with "holoplus:///signup?state=***&code=***"
    - Finally app calls "https://api.holoplus.com/v2/auth/token" to get token

    Doesn't need Authorization header.
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
        session_id="****-***-*******************************-**=",
        url=f"https://account.hololive.net/v1/ep/auth?{query}",
    )


@litestar.get("/v2/auth/callback", summary="/v2/auth/callback", status_code=302)
async def v2__auth__callback(
    *,
    code: Annotated[str, Parameter()],
    state_: Annotated[str, Parameter(query="state")],
) -> Redirect:
    """
    Doesn't need Authorization header.
    """
    query = urllib.parse.urlencode({"code": code, "state": state_})
    return Redirect(f"holoplus:///signup?{query}", status_code=302)


@litestar.post("/v2/auth/token", summary="/v2/auth/token", status_code=200)
async def v2__auth__token(
    data: Annotated[AuthTokenRequest, Body()],
) -> AuthTokenResponse:
    """
    Doesn't need Authorization header.
    """
    return AuthTokenResponse(token="JWT-TOKEN-PLACEHOLDER")


@litestar.get("/v2/me/communities", summary="/v2/me/communities")
async def v2__me__communities(
    *,
    limit: Annotated[int | None, Parameter(examples=[Example(value=30)])] = None,  # TODO: valid range
    token: Annotated[str, Parameter(header="authorization")],
) -> V2CommunitiesResponse:
    return V2CommunitiesResponse(
        items=[
            V2CommunityItem(community=COMMUNITIES_MAP["hololive"]),
            V2CommunityItem(community=COMMUNITIES_MAP["HOLOSTARS"]),
            V2CommunityItem(community=COMMUNITIES_MAP["holoplus"]),
        ]
    )


@litestar.get("/v2/banners", summary="/v2/banners")
async def v2__banners(
    *,
    filter_language: Annotated[str | None, Parameter(examples=[Example(value="en")])] = None,
    token: Annotated[str, Parameter(header="authorization")],
) -> BannersResponse:
    return BannersResponse(
        top=[
            BANNERS_MAP[uuid.UUID("fc7f7724-f78f-40be-8594-aa0e107dd303")],
            BANNERS_MAP[uuid.UUID("6b1791c7-a0bf-4020-82ec-2dc7e8b5d004")],
            BANNERS_MAP[uuid.UUID("22f6a0b0-5781-4747-997d-3d204b906c71")],
            BANNERS_MAP[uuid.UUID("198d15b6-4c76-496a-97bb-32bf0969e4e8")],
            BANNERS_MAP[uuid.UUID("be074072-5f83-41d4-bd99-5431e1c5b588")],
            BANNERS_MAP[uuid.UUID("92b93efd-6739-4e3b-a0cc-1cf90088b882")],
        ],
        middle=[
            BANNERS_MAP[uuid.UUID("7D68B380-402E-47D9-83AD-31B382DC3D39")],
            BANNERS_MAP[uuid.UUID("1F821127-860D-4D09-909F-7F10339D56CA")],
        ],
    )


@litestar.get("/v2/modules", summary="/v2/modules")
async def v2__modules(
    *,
    token: Annotated[str, Parameter(header="authorization")],
) -> ModulesResponse:
    return ModulesResponse(
        items=[
            MODULES_MAP[uuid.UUID("b91175fc-8190-4dde-8e92-01d58ed48f46")],
            MODULES_MAP[uuid.UUID("01bd333b-d391-4ee6-9d82-01b05cdcb445")],
            MODULES_MAP[uuid.UUID("928633f8-124a-4243-b3c4-e5897399815f")],
            MODULES_MAP[uuid.UUID("a6318273-c147-2a63-d7e5-5f0e01ab433b")],
            MODULES_MAP[uuid.UUID("7f4c63df-8929-443a-914f-4b2d07e3d21a")],
            MODULES_MAP[uuid.UUID("a5ac4bf0-237d-464b-9907-adae3bc5b019")],
            MODULES_MAP[uuid.UUID("59f67c37-66bc-4235-8036-115262c08da5")],
            MODULES_MAP[uuid.UUID("6cb7b74b-b112-40b6-9722-e06047c5e049")],
            MODULES_MAP[uuid.UUID("fa7f1c33-e007-4562-b855-1bcaa1b3b819")],
            MODULES_MAP[uuid.UUID("a96b53bf-5045-4a83-b279-024b0215d574")],
            MODULES_MAP[uuid.UUID("723d3431-4be7-4361-9cf3-9a753fc65215")],
            MODULES_MAP[uuid.UUID("ac05ae70-9a4f-11ee-8a54-f2115885f867")],
            MODULES_MAP[uuid.UUID("17ca5776-f868-4b2d-b394-bdf1799203b1")],
            MODULES_MAP[uuid.UUID("7322442b-cb31-4c1c-962b-d1b59c01898c")],
            MODULES_MAP[uuid.UUID("18da6526-7edb-4066-ad63-4b5e84b01d0e")],
            MODULES_MAP[uuid.UUID("29478ced-12dc-4980-8291-f719084a6ab7")],
            MODULES_MAP[uuid.UUID("caeafa55-adf4-4784-8691-b3cfb93082ff")],
            MODULES_MAP[uuid.UUID("f85251e5-2fff-4447-8120-575786170e20")],
        ],
    )


@litestar.get("/v2/groups/{group_id:uuid}", summary="/v2/groups/{group_id:uuid}", raises=[NotFoundException])
async def v2__group(
    *,
    group_id: Annotated[
        uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("e9171551-cb2a-483e-8a77-fdffba8e632b"))])
    ],
    token: Annotated[str, Parameter(header="authorization")],
) -> Group:
    if group_id in GROUPS_MAP:
        return GROUPS_MAP[group_id]
    # TODO: this is a guess
    raise NotFoundException()


@litestar.get("/v2/units/{unit_id:uuid}", summary="/v2/units/{unit_id:uuid}", raises=[NotFoundException])
async def v2__unit(
    *,
    unit_id: Annotated[
        uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("ebe86ce6-0013-46ff-b787-b1e49a6a1bcb"))])
    ],
    token: Annotated[str, Parameter(header="authorization")],
) -> Unit:
    if unit_id in UNITS_MAP:
        return UNITS_MAP[unit_id]
    # TODO: this is a guess
    raise NotFoundException()


ROUTES: list[litestar.handlers.HTTPRouteHandler] = [
    v2__auth,
    v2__auth__callback,
    v2__auth__token,
    v2__me__communities,
    v2__banners,
    v2__modules,
    v2__group,
    v2__unit,
]
