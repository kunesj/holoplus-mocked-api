from __future__ import annotations

import pathlib
import uuid
from typing import Annotated, Self

import litestar.serialization
import msgspec
from litestar.openapi.spec import Example
from litestar.params import Parameter


class TalentChannelCommentsResponseItemUserRole(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("a0a44a43-18bc-4444-96bf-4fb188f3c8d9"))])] = (
        msgspec.field()
    )
    role: Annotated[str, Parameter(examples=[Example(value="none")])] = msgspec.field()


class TalentChannelCommentsResponseItemUserIcon(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("90a8d791-f8f4-4a90-9825-559b463a3f49"))])] = (
        msgspec.field()
    )
    icon_url: Annotated[
        str, Parameter(examples=[Example(value="https://asset.holoplus.com/talents/hololive/tokoyami_towa/motif.png")])
    ] = msgspec.field()


class TalentChannelCommentsResponseItemUser(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("00000000-8def-40c7-bd8d-c44aade2aa10"))])] = (
        msgspec.field()
    )
    name: Annotated[str, Parameter(examples=[Example(value="JimmyFried")])] = msgspec.field()
    role: Annotated[TalentChannelCommentsResponseItemUserRole, Parameter()] = msgspec.field()
    icon: Annotated[TalentChannelCommentsResponseItemUserIcon, Parameter()] = msgspec.field()


class TalentChannelCommentsResponseItemChannel(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("7f237193-e0f7-4127-af78-9f5c255069ac"))])] = (
        msgspec.field()
    )
    name: Annotated[str, Parameter(examples=[Example(value="Kureiji Ollie")])] = msgspec.field()
    channel_type: Annotated[str, Parameter(examples=[Example(value="talent")])] = msgspec.field()


class TalentChannelCommentsResponseItemTranslation(msgspec.Struct, kw_only=True):
    body: Annotated[
        str,
        Parameter(
            examples=[
                Example(
                    value=(
                        "Even though I realized this feature late, this feature is very helpful, "
                        "thank you Ollie for promoting it."
                    )
                )
            ]
        ),
    ] = msgspec.field()


class TalentChannelCommentsResponseItem(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("32cec3c7-5f7f-475c-8ac2-e287f493add0"))])] = (
        msgspec.field()
    )
    parent_id: Annotated[str, Parameter(examples=[Example(value="")])] = msgspec.field()
    body: Annotated[
        str,
        Parameter(
            examples=[
                Example(
                    value=(
                        "Even though I realized this feature late, this feature is very helpful, "
                        "thank you Ollie for promoting it."
                    )
                )
            ]
        ),
    ] = msgspec.field()
    user: Annotated[TalentChannelCommentsResponseItemUser, Parameter()] = msgspec.field()
    channel: Annotated[TalentChannelCommentsResponseItemChannel, Parameter()] = msgspec.field()
    created_at: Annotated[int, Parameter(examples=[Example(value=1757168106)])] = msgspec.field()
    original_language: Annotated[str, Parameter(examples=[Example(value="en")])] = msgspec.field()
    is_translated: Annotated[bool, Parameter(examples=[Example(value=True)])] = msgspec.field()
    translations: Annotated[
        dict[str, TalentChannelCommentsResponseItemTranslation],
        Parameter(
            examples=[Example(value={"en": TalentChannelCommentsResponseItemTranslation(body="Translated body")})]
        ),
    ] = msgspec.field()
    reaction_total: Annotated[int, Parameter(examples=[Example(value=0)])] = msgspec.field()
    reply_count: Annotated[int, Parameter(examples=[Example(value=0)])] = msgspec.field()
    user_reacted_count: Annotated[int, Parameter(examples=[Example(value=0)])] = msgspec.field()


class TalentChannelCommentsResponse(msgspec.Struct, kw_only=True):
    items: Annotated[list[TalentChannelCommentsResponseItem], Parameter()] = msgspec.field()
    next_cursor: Annotated[
        str | None,
        Parameter(
            examples=[
                Example(
                    value="#en#1757126335#96d6d699-98e0-4e07-8c61-152c4ee88a13:1757126335#96d6d699-98e0-4e07-8c61-152c4ee88a13"
                )
            ]
        ),
    ] = msgspec.field(default=None)  # TODO: optional

    @classmethod
    def load_json(cls, path: pathlib.Path) -> Self:
        return litestar.serialization.decode_json(path.read_bytes(), cls, strict=True)
