from __future__ import annotations

import uuid
from typing import Annotated

import msgspec
from litestar.openapi.spec import Example
from litestar.params import Parameter

from holoplus_mocked_api.v1.models import Community


class AuthResponse(msgspec.Struct, kw_only=True):
    session_id: Annotated[str, Parameter(examples=[Example(value="****-***-*******************************-**=")])] = (
        msgspec.field()
    )
    url: Annotated[
        str,
        Parameter(
            examples=[
                Example(
                    value=(
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


class V2Community(Community, kw_only=True):
    channels: Annotated[list[Channel], Parameter()] = msgspec.field()


class V2CommunityList(msgspec.Struct, kw_only=True):
    items: Annotated[list[V2Community], Parameter()] = msgspec.field()


class Channel(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("18eec09c-ce17-4f50-bfc6-8b47457882ed"))])] = (
        msgspec.field()
    )
    created_at: Annotated[int, Parameter(examples=[Example(value=0)])] = msgspec.field()
    updated_at: Annotated[int, Parameter(examples=[Example(value=0)])] = msgspec.field()
    deleted_at: Annotated[int | None, Parameter(examples=[Example(value=None)])] = msgspec.field()
    name: Annotated[str, Parameter(examples=[Example(value="hololive News")])] = msgspec.field()
    guideline: Annotated[
        str,
        Parameter(
            examples=[
                Example(
                    value=(
                        "Get updated on the latest news and information about hololive✨\n"
                        "Engage by leave likes and comments on posts and freely start conversations!🗣️"
                    )
                )
            ]
        ),
    ] = msgspec.field()
    is_official: Annotated[bool, Parameter(examples=[Example(value=True)])] = msgspec.field()


class Banner(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("fc7f7724-f78f-40be-8594-aa0e107dd303"))])] = (
        msgspec.field()
    )
    img_url: Annotated[
        str, Parameter(examples=[Example(value="https://asset.holoplus.com/features/20250901princessvoice5en.png")])
    ] = msgspec.field()
    link: Annotated[
        str,
        Parameter(
            examples=[
                Example(
                    value=(
                        "https://shop.hololivepro.com/products/hololive_princessvoice_indonesianandenglish?"
                        "utm_source=holoplus"
                        "&utm_medium=social"
                        "&utm_campaign=hp_topbanner_global"
                    )
                )
            ]
        ),
    ] = msgspec.field()
    language: Annotated[str, Parameter(examples=[Example(value="en")])] = msgspec.field()
    # TODO: default value is a guess
    sort: Annotated[int, Parameter(examples=[Example(value=0)])] = msgspec.field(default=0)
    started_at: Annotated[int, Parameter(examples=[Example(value=1756717200)])] = msgspec.field()
    expired_at: Annotated[int, Parameter(examples=[Example(value=1757213940)])] = msgspec.field()
    created_at: Annotated[int, Parameter(examples=[Example(value=0)])] = msgspec.field()
    updated_at: Annotated[int, Parameter(examples=[Example(value=0)])] = msgspec.field()


class BannersResponse(msgspec.Struct, kw_only=True):
    top: Annotated[list[Banner], Parameter()] = msgspec.field()
    middle: Annotated[list[Banner], Parameter()] = msgspec.field()


class Module(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("b91175fc-8190-4dde-8e92-01d58ed48f46"))])] = (
        msgspec.field()
    )
    name: Annotated[str, Parameter(examples=[Example(value="Latest News📰")])] = msgspec.field()
    tooltip: Annotated[
        str,
        Parameter(
            examples=[Example(value="The latest posts from all official channels you joined are displayed here.")]
        ),
    ] = msgspec.field()
    enable: Annotated[bool, Parameter(examples=[Example(value=True)])] = msgspec.field()
    priority: Annotated[int, Parameter(examples=[Example(value=1000)])] = msgspec.field()
    display_type: Annotated[str, Parameter(examples=[Example(value="regular")])] = msgspec.field()
    created_at: Annotated[int, Parameter(examples=[Example(value=1672531200)])] = msgspec.field()
    updated_at: Annotated[int, Parameter(examples=[Example(value=1672531200)])] = msgspec.field()


class ModulesList(msgspec.Struct, kw_only=True):
    items: Annotated[list[Module], Parameter()] = msgspec.field()


class GroupUnit(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("ebe86ce6-0013-46ff-b787-b1e49a6a1bcb"))])] = (
        msgspec.field()
    )
    name: Annotated[str, Parameter(examples=[Example(value="hololive Generation 0")])] = msgspec.field()


class Group(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("e9171551-cb2a-483e-8a77-fdffba8e632b"))])] = (
        msgspec.field()
    )
    name: Annotated[str, Parameter(examples=[Example(value="hololive")])] = msgspec.field()
    units: Annotated[list[GroupUnit], Parameter()] = msgspec.field()
    created_at: Annotated[int, Parameter(examples=[Example(value=0)])] = msgspec.field()
    updated_at: Annotated[int, Parameter(examples=[Example(value=0)])] = msgspec.field()


class UnitTalent(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("c9d67e5d-2ef2-407c-ab6c-97f7c3e5c662"))])] = (
        msgspec.field()
    )
    name: Annotated[str, Parameter(examples=[Example(value="Tokino Sora")])] = msgspec.field()
    key_name: Annotated[str, Parameter(examples=[Example(value="tokino_sora")])] = msgspec.field()
    img_url: Annotated[
        str, Parameter(examples=[Example(value="https://asset.holoplus.com/talents/hololive/tokino_sora/icon.png")])
    ] = msgspec.field()
    created_at: Annotated[int | None, Parameter(examples=[Example(value=None)])] = msgspec.field()
    updated_at: Annotated[int | None, Parameter(examples=[Example(value=None)])] = msgspec.field()
    deleted_at: Annotated[int | None, Parameter(examples=[Example(value=None)])] = msgspec.field()
    # TODO: uuid.UUID type is a guess
    group_id: Annotated[uuid.UUID | None, Parameter(examples=[Example(value=None)])] = msgspec.field()


class Unit(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("ebe86ce6-0013-46ff-b787-b1e49a6a1bcb"))])] = (
        msgspec.field()
    )
    name: Annotated[str, Parameter(examples=[Example(value="hololive Generation 0")])] = msgspec.field()
    talents: Annotated[list[UnitTalent], Parameter()] = msgspec.field()
