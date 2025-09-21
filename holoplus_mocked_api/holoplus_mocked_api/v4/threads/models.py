from __future__ import annotations

import pathlib
import uuid
from typing import Annotated, Self

import litestar.serialization
import msgspec
from litestar.openapi.spec import Example
from litestar.params import Parameter


class ThreadsFavoriteResponseItem(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("c7186c9b-6c6d-4269-b4cf-5a2bb97acbd2"))])] = (
        msgspec.field()
    )
    created_at: Annotated[int, Parameter(examples=[Example(value=1757125645)])] = msgspec.field()


class ThreadsFavoriteResponse(msgspec.Struct, kw_only=True):
    items: Annotated[list[ThreadsFavoriteResponseItem], Parameter()] = msgspec.field()
    next_cursor: Annotated[None, Parameter()] = msgspec.field()  # TODO: unknown type


class ThreadsMeResponse(msgspec.Struct, kw_only=True):
    items: Annotated[list[dict], Parameter()] = msgspec.field()  # TODO: unknown type


class ThreadContentComment(msgspec.Struct, kw_only=True):
    body: Annotated[str, Parameter(examples=[Example(value="One of my fav songs from Regloss 🤩")])] = msgspec.field()


class ThreadContent(msgspec.Struct, kw_only=True):
    reply_count: Annotated[int, Parameter(examples=[Example(value=3)])] = msgspec.field()
    picked_up_comment: Annotated[ThreadContentComment | msgspec.UnsetType, Parameter()] = msgspec.field(
        default=msgspec.UNSET
    )
    reaction_total: Annotated[int, Parameter(examples=[Example(value=3057)])] = msgspec.field()
    user_reacted_count: Annotated[int, Parameter(examples=[Example(value=0)])] = msgspec.field()
    is_favorite: Annotated[bool, Parameter(examples=[Example(value=False)])] = msgspec.field()


class ThreadsModulesResponseItem(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("a4d526d1-2c97-476f-ae12-849fdef41eb8"))])] = (
        msgspec.field()
    )
    created_at: Annotated[int, Parameter(examples=[Example(value=1757152800)])] = msgspec.field()


class ThreadsModulesResponse(msgspec.Struct, kw_only=True):
    items: Annotated[list[ThreadsModulesResponseItem], Parameter()] = msgspec.field()
    next_cursor: Annotated[
        str, Parameter(examples=[Example(value="1757077200#1a913d1f-6c90-48de-b015-a9749546fc02")])
    ] = msgspec.field()

    @classmethod
    def load_json(cls, path: pathlib.Path) -> Self:
        return litestar.serialization.decode_json(path.read_bytes(), cls, strict=True)


class ThreadsUpdatedResponseItem(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("e1272fb1-38bc-4e29-aeb8-f8a9443c3340"))])] = (
        msgspec.field()
    )
    created_at: Annotated[int, Parameter(examples=[Example(value=1757165660)])] = msgspec.field()


class ThreadsUpdatedResponse(msgspec.Struct, kw_only=True):
    items: Annotated[list[ThreadsUpdatedResponseItem], Parameter()] = msgspec.field()
    has_next_items: Annotated[bool, Parameter(examples=[Example(value=True)])] = msgspec.field()

    @classmethod
    def load_json(cls, path: pathlib.Path) -> Self:
        return litestar.serialization.decode_json(path.read_bytes(), cls, strict=True)
