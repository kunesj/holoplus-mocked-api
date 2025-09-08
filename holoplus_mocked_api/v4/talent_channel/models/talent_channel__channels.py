from __future__ import annotations

import pathlib
import uuid
from typing import Annotated, Self

import litestar.serialization
import msgspec
from litestar.openapi.spec import Example
from litestar.params import Parameter


class TalentChannelChannelsResponseItemThreadTranslation(msgspec.Struct, kw_only=True):
    title: Annotated[str, Parameter(examples=[Example(value="🔹️ Who do you ship Ollie with?")])] = msgspec.field()


class TalentChannelChannelsResponseItemThread(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("969c000a-22c2-4c8b-a4d0-c6a61cd2e8c0"))])] = (
        msgspec.field()
    )
    original_language: Annotated[str, Parameter(examples=[Example(value="en")])] = msgspec.field()
    title: Annotated[str, Parameter(examples=[Example(value="")])] = msgspec.field()
    translations: Annotated[
        dict[str, TalentChannelChannelsResponseItemThreadTranslation],
        Parameter(
            examples=[
                Example(
                    value={
                        "en": TalentChannelChannelsResponseItemThreadTranslation(title="🔹️ Who do you ship Ollie with?")
                    }
                )
            ]
        ),
    ] = msgspec.field()
    created_at: Annotated[int, Parameter(examples=[Example(value=1757126658)])] = msgspec.field()


class TalentChannelChannelsResponseItemTalent(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("17492aaf-a9bc-48e1-b00c-eeaeefa6b5b0"))])] = (
        msgspec.field()
    )
    name: Annotated[str, Parameter(examples=[Example(value="Kureiji Ollie")])] = msgspec.field()
    icon_url: Annotated[
        str,
        Parameter(
            examples=[Example(value="https://asset.holoplus.com/talents/hololive/kureiji_ollie/icon_20240918.png")]
        ),
    ] = msgspec.field()


class TalentChannelChannelsResponseItemCommunity(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("f30a0c54-73c0-46c1-b413-9e3af0f672ff"))])] = (
        msgspec.field()
    )
    name: Annotated[str, Parameter(examples=[Example(value="hololive")])] = msgspec.field()


class TalentChannelChannelsResponseItem(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("7f237193-e0f7-4127-af78-9f5c255069ac"))])] = (
        msgspec.field()
    )
    name: Annotated[str, Parameter(examples=[Example(value="Kureiji Ollie")])] = msgspec.field()
    icon_url: Annotated[
        str,
        Parameter(
            examples=[Example(value="https://asset.holoplus.com/talents/hololive/kureiji_ollie/icon_20240918.png")]
        ),
    ] = msgspec.field()
    latest_thread: Annotated[TalentChannelChannelsResponseItemThread, Parameter()] = msgspec.field()
    is_my_oshi: Annotated[bool, Parameter(examples=[Example(value=True)])] = msgspec.field()
    talent: Annotated[TalentChannelChannelsResponseItemTalent, Parameter()] = msgspec.field()
    community: Annotated[TalentChannelChannelsResponseItemCommunity, Parameter()] = msgspec.field()


class TalentChannelChannelsResponse(msgspec.Struct, kw_only=True):
    items: Annotated[list[TalentChannelChannelsResponseItem], Parameter()] = msgspec.field()

    @classmethod
    def load_json(cls, path: pathlib.Path) -> Self:
        return litestar.serialization.decode_json(path.read_bytes(), cls, strict=True)
