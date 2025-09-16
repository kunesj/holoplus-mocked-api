from __future__ import annotations

import pathlib
import uuid
from typing import Annotated, Self

import litestar.serialization
import msgspec


class TalentChannelThreadsResponseItemTalent(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("17492aaf-a9bc-48e1-b00c-eeaeefa6b5b0")])] = (
        msgspec.field()
    )
    name: Annotated[str, msgspec.Meta(examples=["Kureiji Ollie"])] = msgspec.field()
    img_url: Annotated[
        str,
        msgspec.Meta(examples=["https://asset.holoplus.com/talents/hololive/kureiji_ollie/icon_20240918.png"]),
    ] = msgspec.field()
    key_name: Annotated[str, msgspec.Meta(examples=["kureiji_ollie"])] = msgspec.field()


class TalentChannelThreadsResponseItemUser(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("3545fcfd-e768-452b-b3f1-de25dd5e4264")])] = (
        msgspec.field()
    )
    name: Annotated[str, msgspec.Meta(examples=["Kureiji Ollie"])] = msgspec.field()
    role: Annotated[str, msgspec.Meta(examples=["talent"])] = msgspec.field()
    icon_url: Annotated[
        str,
        msgspec.Meta(examples=["https://asset.holoplus.com/talents/hololive/kureiji_ollie/icon_20240918.png"]),
    ] = msgspec.field()


class TalentChannelThreadsResponseItemTranslation(msgspec.Struct, kw_only=True):
    title: Annotated[str, msgspec.Meta(examples=["🔹️ Who do you ship Ollie with?"])] = msgspec.field()
    body: Annotated[
        str,
        msgspec.Meta(
            examples=[
                (
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
            ]
        ),
    ] = msgspec.field()


class TalentChannelThreadsResponseItem(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("969c000a-22c2-4c8b-a4d0-c6a61cd2e8c0")])] = (
        msgspec.field()
    )
    title: Annotated[str, msgspec.Meta(examples=["🔹️ Who do you ship Ollie with?"])] = msgspec.field()
    body: Annotated[
        str,
        msgspec.Meta(
            examples=[
                (
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
            ]
        ),
    ] = msgspec.field()
    talents: Annotated[list[TalentChannelThreadsResponseItemTalent], msgspec.Meta()] = msgspec.field()
    user: Annotated[TalentChannelThreadsResponseItemUser, msgspec.Meta()] = msgspec.field()
    created_at: Annotated[int, msgspec.Meta(examples=[1757126658])] = msgspec.field()
    updated_at: Annotated[int, msgspec.Meta(examples=[1757169579])] = msgspec.field()
    original_language: Annotated[str, msgspec.Meta(examples=["en"])] = msgspec.field()
    is_translated: Annotated[bool, msgspec.Meta(examples=[True])] = msgspec.field()
    translations: Annotated[
        dict[str, TalentChannelThreadsResponseItemTranslation],
        msgspec.Meta(
            examples=[
                {"en": TalentChannelThreadsResponseItemTranslation(title="Translated title", body="Translated body")}
            ]
        ),
    ] = msgspec.field()
    reaction_total: Annotated[int, msgspec.Meta(examples=[21311])] = msgspec.field()
    reply_count: Annotated[int, msgspec.Meta(examples=[98])] = msgspec.field()
    is_favorite: Annotated[bool, msgspec.Meta(examples=[False])] = msgspec.field()
    user_reacted_count: Annotated[int, msgspec.Meta(examples=[0])] = msgspec.field()


class TalentChannelThreadsResponseChannel(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("7f237193-e0f7-4127-af78-9f5c255069ac")])] = (
        msgspec.field()
    )
    name: Annotated[str, msgspec.Meta(examples=["Kureiji Ollie"])] = msgspec.field()
    channel_type: Annotated[str, msgspec.Meta(examples=["talent"])] = msgspec.field()
    icon_url: Annotated[
        str,
        msgspec.Meta(examples=["https://asset.holoplus.com/talents/hololive/kureiji_ollie/icon_20240918.png"]),
    ] = msgspec.field()


class TalentChannelThreadsResponse(msgspec.Struct, kw_only=True):
    items: Annotated[list[TalentChannelThreadsResponseItem], msgspec.Meta()] = msgspec.field()
    channel: Annotated[TalentChannelThreadsResponseChannel, msgspec.Meta()] = msgspec.field()

    @classmethod
    def load_json(cls, path: pathlib.Path) -> Self:
        return litestar.serialization.decode_json(path.read_bytes(), cls, strict=True)
