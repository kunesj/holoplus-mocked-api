from __future__ import annotations

import pathlib
import uuid
from typing import Annotated, Self

import litestar.serialization
import msgspec
from litestar.openapi.spec import Example
from litestar.params import Parameter


class ThreadCategory(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("805c061d-a33a-47be-a10a-cfd5d12c631c"))])] = (
        msgspec.field()
    )
    name: Annotated[str, Parameter(examples=[Example(value="Merch")])] = msgspec.field()
    is_official: Annotated[bool, Parameter(examples=[Example(value=False)])] = msgspec.field()
    sort: Annotated[int, Parameter(examples=[Example(value=8)])] = msgspec.field()


class ThreadChannelCommunity(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("f30a0c54-73c0-46c1-b413-9e3af0f672ff"))])] = (
        msgspec.field()
    )
    icon_url: Annotated[
        str, Parameter(examples=[Example(value="https://asset.holoplus.com/communities/hololive/icon_hololive.png")])
    ] = msgspec.field()


class ThreadChannel(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("2f495a98-f005-4ef4-b164-be922b823b42"))])] = (
        msgspec.field()
    )
    name: Annotated[str, Parameter(examples=[Example(value="hololive Chat")])] = msgspec.field()
    guideline: Annotated[
        str,
        Parameter(
            examples=[
                Example(
                    value=(
                        "Post anything about hololive! \nFeel free to talk about streams, live events, merch info, and "
                        "much more💬\n"
                        "\n"
                        "■ Consider the following and create a positive community for everyone❗\n"
                        "💖Share exciting news and favorite moments✨\n"
                        "💖Support live concerts and events together 🎉\n"
                        "💖Report or block harmful posts from (...) on posts!🔕"
                    )
                )
            ]
        ),
    ] = msgspec.field()
    sort: Annotated[int, Parameter(examples=[Example(value=5)])] = msgspec.field()
    created_at: Annotated[int, Parameter(examples=[Example(value=1672499200)])] = msgspec.field()
    updated_at: Annotated[int, Parameter(examples=[Example(value=1672499200)])] = msgspec.field()
    deleted_at: Annotated[int | None, Parameter(examples=[Example(value=None)])] = msgspec.field()
    community: Annotated[ThreadChannelCommunity, Parameter()] = msgspec.field()
    channel_type: Annotated[str, Parameter(examples=[Example(value="open")])] = msgspec.field()
    icon_url: Annotated[str, Parameter(examples=[Example(value="")])] = msgspec.field()


class ThreadImage(msgspec.Struct, kw_only=True):
    url: Annotated[
        str,
        Parameter(
            examples=[
                Example(value="https://asset.holoplus.com/threads/26037de6-61dc-4f12-adf4-d691a0af5252/original.jpeg")
            ]
        ),
    ] = msgspec.field()


class ThreadTalent(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("17492aaf-a9bc-48e1-b00c-eeaeefa6b5b0"))])] = (
        msgspec.field()
    )
    name: Annotated[str, Parameter(examples=[Example(value="Kureiji Ollie")])] = msgspec.field()
    key_name: Annotated[str, Parameter(examples=[Example(value="kureiji_ollie")])] = msgspec.field()
    img_url: Annotated[
        str,
        Parameter(
            examples=[Example(value="https://asset.holoplus.com/talents/hololive/kureiji_ollie/icon_20240918.png")]
        ),
    ] = msgspec.field()


class ThreadUserIcon(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("0b4a2e27-7ff3-491a-a056-8d534d59a87f"))])] = (
        msgspec.field()
    )
    icon_url: Annotated[
        str, Parameter(examples=[Example(value="https://asset.holoplus.com/talents/hololive/kureiji_ollie/motif.png")])
    ] = msgspec.field()


class ThreadUserRole(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("a0a44a43-18bc-4444-96bf-4fb188f3c8d9"))])] = (
        msgspec.field()
    )
    name: Annotated[str, Parameter(examples=[Example(value="none")])] = msgspec.field()


class ThreadUser(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("00000000-3945-4173-af80-ee683388cb4b"))])] = (
        msgspec.field()
    )
    name: Annotated[str, Parameter(examples=[Example(value="Jimmy")])] = msgspec.field()
    icon: Annotated[ThreadUserIcon, Parameter()] = msgspec.field()
    role: Annotated[ThreadUserRole, Parameter()] = msgspec.field()


class ThreadTranslation(msgspec.Struct, kw_only=True):
    title: Annotated[str, Parameter(examples=[Example(value="🔹️ What do you see Ollie as?")])] = msgspec.field()
    body: Annotated[
        str,
        Parameter(
            examples=[
                Example(
                    value=(
                        "We're testing the survey feature on stream! Let me know your answers!✨️\n"
                        "\n"
                        "[[holoplus_survey_start]]\n"
                        "A. Little Sister\n"
                        "B. Older Sister\n"
                        "C. Friend\n"
                        "D. Girlfriend\n"
                        "E. Wife\n"
                        "F. Rival\n"
                        "G. Queen\n"
                        "H. Princess\n"
                        "I. Goddess\n"
                        "J. Enemy\n"
                        "[[holoplus_survey_end]]"
                    )
                )
            ]
        ),
    ] = msgspec.field()


class Thread(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("e1272fb1-38bc-4e29-aeb8-f8a9443c3340"))])] = (
        msgspec.field()
    )
    title: Annotated[str, Parameter(examples=[Example(value="Survey Results")])] = msgspec.field()
    body: Annotated[
        str,
        Parameter(
            examples=[
                Example(
                    value=(
                        "Is there any way to see survey results after it’s ended? I don’t see one on here, but maybe "
                        "I’m missing it?"
                    )
                )
            ]
        ),
    ] = msgspec.field()
    category: Annotated[ThreadCategory | msgspec.UnsetType, Parameter()] = msgspec.field(default=msgspec.UNSET)
    channel: Annotated[ThreadChannel, Parameter()] = msgspec.field()
    images: Annotated[list[ThreadImage], Parameter()] = msgspec.field()
    talents: Annotated[list[ThreadTalent], Parameter()] = msgspec.field()
    user: Annotated[ThreadUser, Parameter()] = msgspec.field()
    created_at: Annotated[int, Parameter(examples=[Example(value=1757165660)])] = msgspec.field()
    updated_at: Annotated[int, Parameter(examples=[Example(value=1757168509)])] = msgspec.field()
    original_language: Annotated[str, Parameter(examples=[Example(value="en")])] = msgspec.field()
    is_translated: Annotated[bool, Parameter(examples=[Example(value=False)])] = msgspec.field()
    translations: Annotated[
        dict[str, ThreadTranslation] | msgspec.UnsetType,
        Parameter(
            examples=[Example(value={"en": ThreadTranslation(title="Translated title", body="Translated body")})]
        ),
    ] = msgspec.field(default=msgspec.UNSET)

    @classmethod
    def load_json(cls, path: pathlib.Path) -> Self:
        return litestar.serialization.decode_json(path.read_bytes(), cls, strict=True)
