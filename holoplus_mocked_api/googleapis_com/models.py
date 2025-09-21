# ruff: noqa: N815

from __future__ import annotations

from typing import Annotated, Literal

import msgspec


class VerifyCustomTokenRequest(msgspec.Struct, kw_only=True):
    instanceId: Annotated[str | msgspec.UnsetType, msgspec.Meta()] = msgspec.field(default=msgspec.UNSET)
    returnSecureToken: Annotated[bool, msgspec.Meta(examples=[True])] = msgspec.field()
    token: Annotated[str, msgspec.Meta(examples=["<JWT-TOKEN>"])] = msgspec.field()
    delegatedProjectNumber: Annotated[str | msgspec.UnsetType, msgspec.Meta()] = msgspec.field(default=msgspec.UNSET)


class VerifyCustomTokenResponse(msgspec.Struct, kw_only=True):
    expiresIn: Annotated[str, msgspec.Meta(examples=["3600"])] = msgspec.field()
    idToken: Annotated[str, msgspec.Meta(examples=["<JWT-ID-TOKEN>"])] = msgspec.field()
    kind: Annotated[Literal["identitytoolkit#VerifyCustomTokenResponse"], msgspec.Meta()] = msgspec.field()
    refreshToken: Annotated[str, msgspec.Meta(examples=["<JWT-REFRESH-TOKEN>"])] = msgspec.field()
    isNewUser: Annotated[bool, msgspec.Meta(examples=[False])] = msgspec.field()


class TokenRequest(msgspec.Struct, kw_only=True):
    grantType: Annotated[str, msgspec.Meta(examples=["refresh_token"])] = msgspec.field()
    refreshToken: Annotated[str, msgspec.Meta(examples=["<JWT-REFRESH-TOKEN>"])] = msgspec.field()


class TokenResponse(msgspec.Struct, kw_only=True):
    id_token: Annotated[str, msgspec.Meta(examples=["<JWT-ID-TOKEN>"])] = msgspec.field()
    access_token: Annotated[str, msgspec.Meta(examples=["<JWT-ACCESS-TOKEN>"])] = msgspec.field()
    refresh_token: Annotated[str, msgspec.Meta(examples=["<JWT-REFRESH-TOKEN>"])] = msgspec.field()
    token_type: Annotated[str, msgspec.Meta(examples=["Bearer"])] = msgspec.field()
    expires_in: Annotated[str, msgspec.Meta(examples=["3600"])] = msgspec.field()
    user_id: Annotated[str, msgspec.Meta(examples=["00000000-bcd7-4efe-ad3a-a21d4b15049e"])] = msgspec.field()
    project_id: Annotated[str, msgspec.Meta(examples=["102023860511"])] = msgspec.field()
