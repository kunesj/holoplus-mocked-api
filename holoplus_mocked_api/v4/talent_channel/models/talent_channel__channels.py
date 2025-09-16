from __future__ import annotations

import pathlib
import uuid
from typing import Annotated, Self

import litestar.serialization
import msgspec


class TalentChannelChannelsResponseItemThreadTranslation(msgspec.Struct, kw_only=True):
    title: Annotated[str, msgspec.Meta(examples=["🔹️ Who do you ship Ollie with?"])] = msgspec.field()


class TalentChannelChannelsResponseItemThread(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("969c000a-22c2-4c8b-a4d0-c6a61cd2e8c0")])] = (
        msgspec.field()
    )
    original_language: Annotated[str, msgspec.Meta(examples=["en"])] = msgspec.field()
    title: Annotated[str, msgspec.Meta(examples=[""])] = msgspec.field()
    translations: Annotated[
        dict[str, TalentChannelChannelsResponseItemThreadTranslation],
        msgspec.Meta(
            examples=[
                {"en": TalentChannelChannelsResponseItemThreadTranslation(title="🔹️ Who do you ship Ollie with?")}
            ]
        ),
    ] = msgspec.field()
    created_at: Annotated[int, msgspec.Meta(examples=[1757126658])] = msgspec.field()


class TalentChannelChannelsResponseItemTalent(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("17492aaf-a9bc-48e1-b00c-eeaeefa6b5b0")])] = (
        msgspec.field()
    )
    name: Annotated[str, msgspec.Meta(examples=["Kureiji Ollie"])] = msgspec.field()
    icon_url: Annotated[
        str,
        msgspec.Meta(examples=["https://asset.holoplus.com/talents/hololive/kureiji_ollie/icon_20240918.png"]),
    ] = msgspec.field()


class TalentChannelChannelsResponseItemCommunity(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("f30a0c54-73c0-46c1-b413-9e3af0f672ff")])] = (
        msgspec.field()
    )
    name: Annotated[str, msgspec.Meta(examples=["hololive"])] = msgspec.field()


class TalentChannelChannelsResponseItem(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("7f237193-e0f7-4127-af78-9f5c255069ac")])] = (
        msgspec.field()
    )
    name: Annotated[str, msgspec.Meta(examples=["Kureiji Ollie"])] = msgspec.field()
    icon_url: Annotated[
        str,
        msgspec.Meta(examples=["https://asset.holoplus.com/talents/hololive/kureiji_ollie/icon_20240918.png"]),
    ] = msgspec.field()
    latest_thread: Annotated[TalentChannelChannelsResponseItemThread, msgspec.Meta()] = msgspec.field()
    is_my_oshi: Annotated[bool, msgspec.Meta(examples=[True])] = msgspec.field()
    talent: Annotated[TalentChannelChannelsResponseItemTalent, msgspec.Meta()] = msgspec.field()
    community: Annotated[TalentChannelChannelsResponseItemCommunity, msgspec.Meta()] = msgspec.field()


class TalentChannelChannelsResponse(msgspec.Struct, kw_only=True):
    items: Annotated[list[TalentChannelChannelsResponseItem], msgspec.Meta()] = msgspec.field()

    @classmethod
    def load_json(cls, path: pathlib.Path) -> Self:
        return litestar.serialization.decode_json(path.read_bytes(), cls, strict=True)
