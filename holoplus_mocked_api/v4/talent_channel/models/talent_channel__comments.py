from __future__ import annotations

import pathlib
import uuid
from typing import Annotated, Self

import litestar.serialization
import msgspec


class TalentChannelCommentsResponseItemUserRole(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("a0a44a43-18bc-4444-96bf-4fb188f3c8d9")])] = (
        msgspec.field()
    )
    role: Annotated[str, msgspec.Meta(examples=["none"])] = msgspec.field()


class TalentChannelCommentsResponseItemUserIcon(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("90a8d791-f8f4-4a90-9825-559b463a3f49")])] = (
        msgspec.field()
    )
    icon_url: Annotated[
        str, msgspec.Meta(examples=["https://asset.holoplus.com/talents/hololive/tokoyami_towa/motif.png"])
    ] = msgspec.field()


class TalentChannelCommentsResponseItemUser(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("00000000-8def-40c7-bd8d-c44aade2aa10")])] = (
        msgspec.field()
    )
    name: Annotated[str, msgspec.Meta(examples=["JimmyFried"])] = msgspec.field()
    role: Annotated[TalentChannelCommentsResponseItemUserRole, msgspec.Meta()] = msgspec.field()
    icon: Annotated[TalentChannelCommentsResponseItemUserIcon, msgspec.Meta()] = msgspec.field()


class TalentChannelCommentsResponseItemChannel(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("7f237193-e0f7-4127-af78-9f5c255069ac")])] = (
        msgspec.field()
    )
    name: Annotated[str, msgspec.Meta(examples=["Kureiji Ollie"])] = msgspec.field()
    channel_type: Annotated[str, msgspec.Meta(examples=["talent"])] = msgspec.field()


class TalentChannelCommentsResponseItemTranslation(msgspec.Struct, kw_only=True):
    body: Annotated[
        str,
        msgspec.Meta(
            examples=[
                (
                    "Even though I realized this feature late, this feature is very helpful, "
                    "thank you Ollie for promoting it."
                )
            ]
        ),
    ] = msgspec.field()


class TalentChannelCommentsResponseItem(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("32cec3c7-5f7f-475c-8ac2-e287f493add0")])] = (
        msgspec.field()
    )
    parent_id: Annotated[str, msgspec.Meta(examples=[""])] = msgspec.field()
    body: Annotated[
        str,
        msgspec.Meta(
            examples=[
                (
                    "Even though I realized this feature late, this feature is very helpful, "
                    "thank you Ollie for promoting it."
                )
            ]
        ),
    ] = msgspec.field()
    user: Annotated[TalentChannelCommentsResponseItemUser, msgspec.Meta()] = msgspec.field()
    channel: Annotated[TalentChannelCommentsResponseItemChannel, msgspec.Meta()] = msgspec.field()
    created_at: Annotated[int, msgspec.Meta(examples=[1757168106])] = msgspec.field()
    original_language: Annotated[str, msgspec.Meta(examples=["en"])] = msgspec.field()
    is_translated: Annotated[bool, msgspec.Meta(examples=[True])] = msgspec.field()
    translations: Annotated[
        dict[str, TalentChannelCommentsResponseItemTranslation],
        msgspec.Meta(examples=[{"en": TalentChannelCommentsResponseItemTranslation(body="Translated body")}]),
    ] = msgspec.field()
    reaction_total: Annotated[int, msgspec.Meta(examples=[0])] = msgspec.field()
    reply_count: Annotated[int, msgspec.Meta(examples=[0])] = msgspec.field()
    user_reacted_count: Annotated[int, msgspec.Meta(examples=[0])] = msgspec.field()


class TalentChannelCommentsResponse(msgspec.Struct, kw_only=True):
    items: Annotated[list[TalentChannelCommentsResponseItem], msgspec.Meta()] = msgspec.field()
    next_cursor: Annotated[
        str | msgspec.UnsetType,
        msgspec.Meta(
            examples=[
                "#en#1757126335#96d6d699-98e0-4e07-8c61-152c4ee88a13:1757126335#96d6d699-98e0-4e07-8c61-152c4ee88a13"
            ]
        ),
    ] = msgspec.field(default=msgspec.UNSET)

    @classmethod
    def load_json(cls, path: pathlib.Path) -> Self:
        return litestar.serialization.decode_json(path.read_bytes(), cls, strict=True)
