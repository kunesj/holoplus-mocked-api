from __future__ import annotations

import pathlib
import uuid
from typing import Annotated, Self

import litestar.serialization
import msgspec
from litestar.openapi.spec import Example
from litestar.params import Parameter


class CommentContent(msgspec.Struct, kw_only=True):
    comment_total: Annotated[int, Parameter(examples=[Example(value=0)])] = msgspec.field()
    reaction_total: Annotated[int, Parameter(examples=[Example(value=6)])] = msgspec.field()
    user_reacted_count: Annotated[int, Parameter(examples=[Example(value=0)])] = msgspec.field()


class CommentsMeResponseItemThread(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("3777da4d-60e3-11ef-8c79-0a58a9feac02"))])] = (
        msgspec.field()
    )
    title: Annotated[str, Parameter(examples=[Example(value="What country are you from?")])] = msgspec.field()


class CommentsMeResponseItemChannel(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("2f495a98-f005-4ef4-b164-be922b823b42"))])] = (
        msgspec.field()
    )
    name: Annotated[str, Parameter(examples=[Example(value="hololive Chat")])] = msgspec.field()
    channel_type: Annotated[str, Parameter(examples=[Example(value="open")])] = msgspec.field()
    icon_url: Annotated[str, Parameter(examples=[Example(value="")])] = msgspec.field()


class CommentsMeResponseItemCommunity(msgspec.Struct, kw_only=True):
    icon_url: Annotated[
        str, Parameter(examples=[Example(value="https://asset.holoplus.com/communities/hololive/icon_hololive.png")])
    ] = msgspec.field()


class CommentsMeResponseItem(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("cfdd2f8b-ee45-4e3f-b4df-c150f826e224"))])] = (
        msgspec.field()
    )
    body: Annotated[str, Parameter(examples=[Example(value="Czechia 🇨🇿")])] = msgspec.field()
    created_at: Annotated[int, Parameter(examples=[Example(value=1724375313)])] = msgspec.field()
    parent_id: Annotated[str, Parameter(examples=[Example(value="")])] = msgspec.field()
    thread: Annotated[CommentsMeResponseItemThread, Parameter()] = msgspec.field()
    channel: Annotated[CommentsMeResponseItemChannel, Parameter()] = msgspec.field()
    community: Annotated[CommentsMeResponseItemCommunity, Parameter()] = msgspec.field()
    is_transition_disabled: Annotated[bool, Parameter(examples=[Example(value=False)])] = msgspec.field()


class CommentsMeResponse(msgspec.Struct, kw_only=True):
    items: Annotated[list[CommentsMeResponseItem], Parameter()] = msgspec.field()

    @classmethod
    def load_json(cls, path: pathlib.Path) -> Self:
        return litestar.serialization.decode_json(path.read_bytes(), cls, strict=True)


class CommentUserRole(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("a0a44a43-18bc-4444-96bf-4fb188f3c8d9"))])] = (
        msgspec.field()
    )
    role: Annotated[str, Parameter(examples=[Example(value="none")])] = msgspec.field()


class CommentUserIcon(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("90a8d791-f8f4-4a90-9825-559b463a3f49"))])] = (
        msgspec.field()
    )
    icon_url: Annotated[
        str, Parameter(examples=[Example(value="https://asset.holoplus.com/talents/hololive/tokoyami_towa/motif.png")])
    ] = msgspec.field()


class CommentUser(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("00000000-8def-40c7-bd8d-c44aade2aa10"))])] = (
        msgspec.field()
    )
    name: Annotated[str, Parameter(examples=[Example(value="JimmyFried")])] = msgspec.field()
    role: Annotated[CommentUserRole, Parameter()] = msgspec.field()
    icon: Annotated[CommentUserIcon, Parameter()] = msgspec.field()


class Comment(msgspec.Struct, kw_only=True):
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
    user: Annotated[CommentUser, Parameter()] = msgspec.field()
    channel: Annotated[None, Parameter()] = msgspec.field()  # TODO: unknown type
    created_at: Annotated[int, Parameter(examples=[Example(value=1757168106)])] = msgspec.field()
    original_language: Annotated[None, Parameter()] = msgspec.field()  # TODO: unknown type
    is_translated: Annotated[None, Parameter()] = msgspec.field()  # TODO: unknown type
    translations: Annotated[None, Parameter()] = msgspec.field()  # TODO: unknown type


class CommentsResponse(msgspec.Struct, kw_only=True):
    items: Annotated[list[Comment], Parameter()] = msgspec.field()

    @classmethod
    def load_json(cls, path: pathlib.Path) -> Self:
        return litestar.serialization.decode_json(path.read_bytes(), cls, strict=True)
