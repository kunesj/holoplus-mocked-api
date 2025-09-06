from __future__ import annotations

from typing import Annotated

import msgspec
from litestar.openapi.spec import Example
from litestar.params import Parameter


class AuthResponse(msgspec.Struct, kw_only=True):
    session_id: Annotated[str, Parameter(examples=[Example(value="0000-000-0000000000000000000000000000000-00=")])] = (
        msgspec.field()
    )
    url: Annotated[
        str,
        Parameter(
            examples=[
                Example(
                    value=(
                        "https://account.hololive.net/v1/ep/auth?"
                        "\u0026client_id=H7HAzZpy8DnSDIoAohtafeU4pPBb1Ch9"
                        "\u0026code_challenge=**-****************************************"
                        "\u0026code_challenge_method=S256"
                        "\u0026nonce=*******************************************"
                        "\u0026redirect_uri=https%3A%2F%2Fapi.holoplus.com%2Fv2%2Fauth%2Fcallback"
                        "\u0026response_type=code"
                        "\u0026scope=openid+profile"
                        "\u0026state=********************************************"
                    )
                )
            ]
        ),
    ] = msgspec.field()


class AuthTokenRequest(msgspec.Struct, kw_only=True):
    code: Annotated[str, Parameter()] = msgspec.field()
    session_id: Annotated[str, Parameter()] = msgspec.field()
    state: Annotated[str, Parameter()] = msgspec.field()


class AuthTokenResponse(msgspec.Struct, kw_only=True):
    token: Annotated[str, Parameter()] = msgspec.field()
