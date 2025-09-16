from __future__ import annotations

import pathlib
import uuid
from typing import Annotated, Self

import litestar.serialization
import msgspec


class AuthResponse(msgspec.Struct, kw_only=True):
    session_id: Annotated[str, msgspec.Meta(examples=["****-***-*******************************-**="])] = (
        msgspec.field()
    )
    url: Annotated[
        str,
        msgspec.Meta(
            examples=[
                (
                    "https://account.hololive.net/v1/ep/auth?"
                    "&client_id=H7HAzZpy8DnSDIoAohtafeU4pPBb1Ch9"
                    "&code_challenge=**-****************************************"
                    "&code_challenge_method=S256"
                    "&nonce=*******************************************"
                    "&redirect_uri=https%3A%2F%2Fapi.holoplus.com%2Fv2%2Fauth%2Fcallback"
                    "&response_type=code"
                    "&scope=openid+profile"
                    "&state=********************************************"
                )
            ]
        ),
    ] = msgspec.field()


class AuthTokenRequest(msgspec.Struct, kw_only=True):
    code: Annotated[str, msgspec.Meta()] = msgspec.field()
    session_id: Annotated[str, msgspec.Meta()] = msgspec.field()
    state: Annotated[str, msgspec.Meta()] = msgspec.field()


class AuthTokenResponse(msgspec.Struct, kw_only=True):
    token: Annotated[str, msgspec.Meta()] = msgspec.field()


class Community(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("3f255c77-3b3e-4585-8e4f-7e5a4adcef58")])] = (
        msgspec.field()
    )
    name: Annotated[str, msgspec.Meta(examples=["holoplus"])] = msgspec.field()
    icon_url: Annotated[
        str, msgspec.Meta(examples=["https://asset.holoplus.com/communities/holoplus/icon_holoplus.png"])
    ] = msgspec.field()
    img_url: Annotated[str, msgspec.Meta(examples=[""])] = msgspec.field()
    is_official: Annotated[bool, msgspec.Meta(examples=[True])] = msgspec.field()
    group_id: Annotated[str, msgspec.Meta(examples=[""])] = msgspec.field()
    created_at: Annotated[int, msgspec.Meta(examples=[0])] = msgspec.field()
    updated_at: Annotated[int, msgspec.Meta(examples=[0])] = msgspec.field()
    deleted_at: Annotated[int | None, msgspec.Meta(examples=[None])] = msgspec.field()
    channels: Annotated[list[Channel], msgspec.Meta()] = msgspec.field()


class CommunitiesResponseItem(msgspec.Struct, kw_only=True):
    community: Annotated[Community, msgspec.Meta()] = msgspec.field()


class CommunitiesResponse(msgspec.Struct, kw_only=True):
    items: Annotated[list[CommunitiesResponseItem], msgspec.Meta()] = msgspec.field()

    @classmethod
    def load_json(cls, path: pathlib.Path) -> Self:
        return litestar.serialization.decode_json(path.read_bytes(), cls, strict=True)


class Channel(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("18eec09c-ce17-4f50-bfc6-8b47457882ed")])] = (
        msgspec.field()
    )
    created_at: Annotated[int, msgspec.Meta(examples=[0])] = msgspec.field()
    updated_at: Annotated[int, msgspec.Meta(examples=[0])] = msgspec.field()
    deleted_at: Annotated[int | None, msgspec.Meta(examples=[None])] = msgspec.field()
    name: Annotated[str, msgspec.Meta(examples=["hololive News"])] = msgspec.field()
    guideline: Annotated[
        str,
        msgspec.Meta(
            examples=[
                (
                    "Get updated on the latest news and information about hololive✨\n"
                    "Engage by leave likes and comments on posts and freely start conversations!🗣️"
                )
            ]
        ),
    ] = msgspec.field()
    is_official: Annotated[bool, msgspec.Meta(examples=[True])] = msgspec.field()


class Banner(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("fc7f7724-f78f-40be-8594-aa0e107dd303")])] = (
        msgspec.field()
    )
    img_url: Annotated[
        str, msgspec.Meta(examples=["https://asset.holoplus.com/features/20250901princessvoice5en.png"])
    ] = msgspec.field()
    link: Annotated[
        str,
        msgspec.Meta(
            examples=[
                (
                    "https://shop.hololivepro.com/products/hololive_princessvoice_indonesianandenglish?"
                    "utm_source=holoplus"
                    "&utm_medium=social"
                    "&utm_campaign=hp_topbanner_global"
                )
            ]
        ),
    ] = msgspec.field()
    language: Annotated[str, msgspec.Meta(examples=["en"])] = msgspec.field()
    sort: Annotated[int | msgspec.UnsetType, msgspec.Meta(examples=[0])] = msgspec.field(default=msgspec.UNSET)
    started_at: Annotated[int, msgspec.Meta(examples=[1756717200])] = msgspec.field()
    expired_at: Annotated[int, msgspec.Meta(examples=[1757213940])] = msgspec.field()
    created_at: Annotated[int, msgspec.Meta(examples=[0])] = msgspec.field()
    updated_at: Annotated[int, msgspec.Meta(examples=[0])] = msgspec.field()


class BannersResponse(msgspec.Struct, kw_only=True):
    top: Annotated[list[Banner], msgspec.Meta()] = msgspec.field()
    middle: Annotated[list[Banner], msgspec.Meta()] = msgspec.field()

    @classmethod
    def load_json(cls, path: pathlib.Path) -> Self:
        return litestar.serialization.decode_json(path.read_bytes(), cls, strict=True)


class Module(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("b91175fc-8190-4dde-8e92-01d58ed48f46")])] = (
        msgspec.field()
    )
    name: Annotated[str, msgspec.Meta(examples=["Latest News📰"])] = msgspec.field()
    tooltip: Annotated[
        str,
        msgspec.Meta(examples=["The latest posts from all official channels you joined are displayed here."]),
    ] = msgspec.field()
    enable: Annotated[bool, msgspec.Meta(examples=[True])] = msgspec.field()
    priority: Annotated[int, msgspec.Meta(examples=[1000])] = msgspec.field()
    display_type: Annotated[str, msgspec.Meta(examples=["regular"])] = msgspec.field()
    created_at: Annotated[int, msgspec.Meta(examples=[1672531200])] = msgspec.field()
    updated_at: Annotated[int, msgspec.Meta(examples=[1672531200])] = msgspec.field()


class ModulesResponse(msgspec.Struct, kw_only=True):
    items: Annotated[list[Module], msgspec.Meta()] = msgspec.field()

    @classmethod
    def load_json(cls, path: pathlib.Path) -> Self:
        return litestar.serialization.decode_json(path.read_bytes(), cls, strict=True)


class GroupUnit(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("ebe86ce6-0013-46ff-b787-b1e49a6a1bcb")])] = (
        msgspec.field()
    )
    name: Annotated[str, msgspec.Meta(examples=["hololive Generation 0"])] = msgspec.field()


class Group(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("e9171551-cb2a-483e-8a77-fdffba8e632b")])] = (
        msgspec.field()
    )
    name: Annotated[str, msgspec.Meta(examples=["hololive"])] = msgspec.field()
    units: Annotated[list[GroupUnit], msgspec.Meta()] = msgspec.field()
    created_at: Annotated[int, msgspec.Meta(examples=[0])] = msgspec.field()
    updated_at: Annotated[int, msgspec.Meta(examples=[0])] = msgspec.field()

    @classmethod
    def load_json(cls, path: pathlib.Path) -> Self:
        return litestar.serialization.decode_json(path.read_bytes(), cls, strict=True)


class UnitTalent(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("c9d67e5d-2ef2-407c-ab6c-97f7c3e5c662")])] = (
        msgspec.field()
    )
    name: Annotated[str, msgspec.Meta(examples=["Tokino Sora"])] = msgspec.field()
    key_name: Annotated[str, msgspec.Meta(examples=["tokino_sora"])] = msgspec.field()
    img_url: Annotated[
        str, msgspec.Meta(examples=["https://asset.holoplus.com/talents/hololive/tokino_sora/icon.png"])
    ] = msgspec.field()
    created_at: Annotated[int | None, msgspec.Meta(examples=[None])] = msgspec.field()
    updated_at: Annotated[int | None, msgspec.Meta(examples=[None])] = msgspec.field()
    deleted_at: Annotated[int | None, msgspec.Meta(examples=[None])] = msgspec.field()
    # TODO: uuid.UUID type is a guess
    group_id: Annotated[uuid.UUID | None, msgspec.Meta(examples=[None])] = msgspec.field()


class Unit(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("ebe86ce6-0013-46ff-b787-b1e49a6a1bcb")])] = (
        msgspec.field()
    )
    name: Annotated[str, msgspec.Meta(examples=["hololive Generation 0"])] = msgspec.field()
    talents: Annotated[list[UnitTalent], msgspec.Meta()] = msgspec.field()

    @classmethod
    def load_json(cls, path: pathlib.Path) -> Self:
        return litestar.serialization.decode_json(path.read_bytes(), cls, strict=True)
