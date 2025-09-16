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
