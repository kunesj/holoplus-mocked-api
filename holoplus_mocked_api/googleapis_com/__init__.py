from __future__ import annotations

from typing import Annotated

import litestar
from litestar import status_codes
from litestar.types import ControllerRouterHandler
from litestar.params import Body, Parameter
from litestar.openapi.spec import Example

from .models import VerifyCustomTokenRequest, VerifyCustomTokenResponse, TokenRequest, TokenResponse


@litestar.post(
    "/www.googleapis.com/identitytoolkit/v3/relyingparty/verifyCustomToken",
    summary="/www.googleapis.com/identitytoolkit/v3/relyingparty/verifyCustomToken",
    status_code=status_codes.HTTP_200_OK,
)
async def verifycustomtoken(
    data: Annotated[VerifyCustomTokenRequest, Body()],
    *,
    key: Annotated[str, Parameter(examples=[Example(value="AIzaSyBIBy1CboBwrCShfY1CixfRRynJRF06vx0")])],
) -> VerifyCustomTokenResponse:
    """
    Converts **Firebase** token returned by `/v2/auth/token` into Holoplus tokens.
    See `https://developers.google.com/resources/api-libraries/documentation/identitytoolkit/v3/python/latest/identitytoolkit_v3.relyingparty.html#verifyCustomToken` for more info.
    """
    # TODO: generate parsable tokens
    return VerifyCustomTokenResponse(
        expiresIn="3600",
        idToken="<JWT-ID-TOKEN>",
        kind="identitytoolkit#VerifyCustomTokenResponse",
        refreshToken="<JWT-REFRESH-TOKEN>",
        isNewUser=False,
    )


@litestar.post(
    "/securetoken.googleapis.com/v1/token",
    summary="/securetoken.googleapis.com/v1/token",
    status_code=status_codes.HTTP_200_OK,
)
async def v1_token(
    data: Annotated[TokenRequest, Body()],
    *,
    key: Annotated[str, Parameter(examples=[Example(value="AIzaSyBIBy1CboBwrCShfY1CixfRRynJRF06vx0")])],
) -> TokenResponse:
    """
    Refreshes Holoplus token
    """
    # TODO: generate parsable tokens
    return TokenResponse(
        id_token="<JWT-ID-TOKEN>",
        access_token="<JWT-ACCESS-TOKEN>",
        refresh_token="<JWT-REFRESH-TOKEN>",
        token_type="Bearer",
        expires_in="3600",
        user_id="00000000-bcd7-4efe-ad3a-a21d4b15049e",
        project_id="102023860511",
    )


ROUTES: list[ControllerRouterHandler] = [
    litestar.Router(
        "",
        tags=["www.googleapis.com"],
        route_handlers=[
            verifycustomtoken,
            v1_token,
        ],
    ),
]
