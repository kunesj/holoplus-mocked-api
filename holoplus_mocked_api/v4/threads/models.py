from __future__ import annotations

import uuid
from typing import Annotated

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
    # FIXME: None default is guess
    picked_up_comment: Annotated[ThreadContentComment | None, Parameter()] = msgspec.field(default=None)
    reaction_total: Annotated[int, Parameter(examples=[Example(value=3057)])] = msgspec.field()
    user_reacted_count: Annotated[int, Parameter(examples=[Example(value=0)])] = msgspec.field()
    is_favorite: Annotated[bool, Parameter(examples=[Example(value=False)])] = msgspec.field()
