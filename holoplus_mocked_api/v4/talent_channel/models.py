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


class TalentChannelThreadsNewestResponseItemTalent(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("17492aaf-a9bc-48e1-b00c-eeaeefa6b5b0"))])] = (
        msgspec.field()
    )
    name: Annotated[str, Parameter(examples=[Example(value="Kureiji Ollie")])] = msgspec.field()
    img_url: Annotated[
        str,
        Parameter(
            examples=[Example(value="https://asset.holoplus.com/talents/hololive/kureiji_ollie/icon_20240918.png")]
        ),
    ] = msgspec.field()
    key_name: Annotated[str, Parameter(examples=[Example(value="kureiji_ollie")])] = msgspec.field()


class TalentChannelThreadsNewestResponseItemUser(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("3545fcfd-e768-452b-b3f1-de25dd5e4264"))])] = (
        msgspec.field()
    )
    name: Annotated[str, Parameter(examples=[Example(value="Kureiji Ollie")])] = msgspec.field()
    role: Annotated[str, Parameter(examples=[Example(value="talent")])] = msgspec.field()
    icon_url: Annotated[
        str,
        Parameter(
            examples=[Example(value="https://asset.holoplus.com/talents/hololive/kureiji_ollie/icon_20240918.png")]
        ),
    ] = msgspec.field()


class TalentChannelThreadsNewestResponseItemTranslation(msgspec.Struct, kw_only=True):
    title: Annotated[str, Parameter(examples=[Example(value="🔹️ Who do you ship Ollie with?")])] = msgspec.field()
    body: Annotated[
        str,
        Parameter(
            examples=[
                Example(
                    value=(
                        "Tell me your favorite ship!\n"
                        "\n"
                        "[[holoplus_survey_start]]\n"
                        "A. Ayunda Risu\n"
                        "B. Elizabeth Rose Bloodflame\n"
                        "C. Kaela Kovalskia\n"
                        "D. Nerissa Ravencroft\n"
                        "E. Moona Hoshinova\n"
                        "F. Airani Iofifteen\n"
                        "G. Takanashi Kiara\n"
                        "H. Mori Calliope\n"
                        "I. Jurard T Rexford\n"
                        "J. ME!! [The Listener]\n"
                        "[[holoplus_survey_end]]"
                    )
                )
            ]
        ),
    ] = msgspec.field()


class TalentChannelThreadsNewestResponseItem(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("969c000a-22c2-4c8b-a4d0-c6a61cd2e8c0"))])] = (
        msgspec.field()
    )
    title: Annotated[str, Parameter(examples=[Example(value="🔹️ Who do you ship Ollie with?")])] = msgspec.field()
    body: Annotated[
        str,
        Parameter(
            examples=[
                Example(
                    value=(
                        "Tell me your favorite ship!\n"
                        "\n"
                        "[[holoplus_survey_start]]\n"
                        "A. Ayunda Risu\n"
                        "B. Elizabeth Rose Bloodflame\n"
                        "C. Kaela Kovalskia\n"
                        "D. Nerissa Ravencroft\n"
                        "E. Moona Hoshinova\n"
                        "F. Airani Iofifteen\n"
                        "G. Takanashi Kiara\n"
                        "H. Mori Calliope\n"
                        "I. Jurard T Rexford\n"
                        "J. ME!! [The Listener]\n"
                        "[[holoplus_survey_end]]"
                    )
                )
            ]
        ),
    ] = msgspec.field()
    talents: Annotated[list[TalentChannelThreadsNewestResponseItemTalent], Parameter()] = msgspec.field()
    user: Annotated[TalentChannelThreadsNewestResponseItemUser, Parameter()] = msgspec.field()
    created_at: Annotated[int, Parameter(examples=[Example(value=1757126658)])] = msgspec.field()
    updated_at: Annotated[int, Parameter(examples=[Example(value=1757169579)])] = msgspec.field()
    original_language: Annotated[str, Parameter(examples=[Example(value="en")])] = msgspec.field()
    is_translated: Annotated[bool, Parameter(examples=[Example(value=True)])] = msgspec.field()
    translations: Annotated[
        dict[str, TalentChannelThreadsNewestResponseItemTranslation],
        Parameter(
            examples=[
                Example(
                    value={
                        "en": TalentChannelThreadsNewestResponseItemTranslation(
                            title="Translated title", body="Translated body"
                        )
                    }
                )
            ]
        ),
    ] = msgspec.field()
    reaction_total: Annotated[int, Parameter(examples=[Example(value=21311)])] = msgspec.field()
    reply_count: Annotated[int, Parameter(examples=[Example(value=98)])] = msgspec.field()
    is_favorite: Annotated[bool, Parameter(examples=[Example(value=False)])] = msgspec.field()
    user_reacted_count: Annotated[int, Parameter(examples=[Example(value=0)])] = msgspec.field()


class TalentChannelThreadsNewestResponseChannel(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("7f237193-e0f7-4127-af78-9f5c255069ac"))])] = (
        msgspec.field()
    )
    name: Annotated[str, Parameter(examples=[Example(value="Kureiji Ollie")])] = msgspec.field()
    channel_type: Annotated[str, Parameter(examples=[Example(value="talent")])] = msgspec.field()
    icon_url: Annotated[
        str,
        Parameter(
            examples=[Example(value="https://asset.holoplus.com/talents/hololive/kureiji_ollie/icon_20240918.png")]
        ),
    ] = msgspec.field()


class TalentChannelThreadsNewestResponse(msgspec.Struct, kw_only=True):
    items: Annotated[list[TalentChannelThreadsNewestResponseItem], Parameter()] = msgspec.field()
    channel: Annotated[TalentChannelThreadsNewestResponseChannel, Parameter()] = msgspec.field()

    @classmethod
    def load_json(cls, path: pathlib.Path) -> Self:
        return litestar.serialization.decode_json(path.read_bytes(), cls, strict=True)
