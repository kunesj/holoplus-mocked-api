from __future__ import annotations

import pathlib
import uuid
from typing import Annotated, Self

import litestar.serialization
import msgspec


class CommentContent(msgspec.Struct, kw_only=True):
    comment_total: Annotated[int, msgspec.Meta(examples=[0])] = msgspec.field()
    reaction_total: Annotated[int, msgspec.Meta(examples=[6])] = msgspec.field()
    user_reacted_count: Annotated[int, msgspec.Meta(examples=[0])] = msgspec.field()


class CommentsMeResponseItemThread(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("3777da4d-60e3-11ef-8c79-0a58a9feac02")])] = (
        msgspec.field()
    )
    title: Annotated[str, msgspec.Meta(examples=["What country are you from?"])] = msgspec.field()


class CommentsMeResponseItemChannel(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("2f495a98-f005-4ef4-b164-be922b823b42")])] = (
        msgspec.field()
    )
    name: Annotated[str, msgspec.Meta(examples=["hololive Chat"])] = msgspec.field()
    channel_type: Annotated[str, msgspec.Meta(examples=["open"])] = msgspec.field()
    icon_url: Annotated[str, msgspec.Meta(examples=[""])] = msgspec.field()


class CommentsMeResponseItemCommunity(msgspec.Struct, kw_only=True):
    icon_url: Annotated[
        str, msgspec.Meta(examples=["https://asset.holoplus.com/communities/hololive/icon_hololive.png"])
    ] = msgspec.field()


class CommentsMeResponseItem(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("cfdd2f8b-ee45-4e3f-b4df-c150f826e224")])] = (
        msgspec.field()
    )
    body: Annotated[str, msgspec.Meta(examples=["Czechia 🇨🇿"])] = msgspec.field()
    created_at: Annotated[int, msgspec.Meta(examples=[1724375313])] = msgspec.field()
    parent_id: Annotated[str, msgspec.Meta(examples=[""])] = msgspec.field()
    thread: Annotated[CommentsMeResponseItemThread, msgspec.Meta()] = msgspec.field()
    channel: Annotated[CommentsMeResponseItemChannel, msgspec.Meta()] = msgspec.field()
    community: Annotated[CommentsMeResponseItemCommunity, msgspec.Meta()] = msgspec.field()
    is_transition_disabled: Annotated[bool, msgspec.Meta(examples=[False])] = msgspec.field()


class CommentsMeResponse(msgspec.Struct, kw_only=True):
    items: Annotated[list[CommentsMeResponseItem], msgspec.Meta()] = msgspec.field()

    @classmethod
    def load_json(cls, path: pathlib.Path) -> Self:
        return litestar.serialization.decode_json(path.read_bytes(), cls, strict=True)


class CommentUserRole(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("a0a44a43-18bc-4444-96bf-4fb188f3c8d9")])] = (
        msgspec.field()
    )
    role: Annotated[str, msgspec.Meta(examples=["none"])] = msgspec.field()


class CommentUserIcon(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("90a8d791-f8f4-4a90-9825-559b463a3f49")])] = (
        msgspec.field()
    )
    icon_url: Annotated[
        str, msgspec.Meta(examples=["https://asset.holoplus.com/talents/hololive/tokoyami_towa/motif.png"])
    ] = msgspec.field()


class CommentUser(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("00000000-8def-40c7-bd8d-c44aade2aa10")])] = (
        msgspec.field()
    )
    name: Annotated[str, msgspec.Meta(examples=["JimmyFried"])] = msgspec.field()
    role: Annotated[CommentUserRole, msgspec.Meta()] = msgspec.field()
    icon: Annotated[CommentUserIcon, msgspec.Meta()] = msgspec.field()


class Comment(msgspec.Struct, kw_only=True):
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
    user: Annotated[CommentUser, msgspec.Meta()] = msgspec.field()
    channel: Annotated[None, msgspec.Meta()] = msgspec.field()  # TODO: unknown type
    created_at: Annotated[int, msgspec.Meta(examples=[1757168106])] = msgspec.field()
    original_language: Annotated[None, msgspec.Meta()] = msgspec.field()  # TODO: unknown type
    is_translated: Annotated[None, msgspec.Meta()] = msgspec.field()  # TODO: unknown type
    translations: Annotated[None, msgspec.Meta()] = msgspec.field()  # TODO: unknown type


class CommentsResponse(msgspec.Struct, kw_only=True):
    items: Annotated[list[Comment], msgspec.Meta()] = msgspec.field()

    @classmethod
    def load_json(cls, path: pathlib.Path) -> Self:
        return litestar.serialization.decode_json(path.read_bytes(), cls, strict=True)
