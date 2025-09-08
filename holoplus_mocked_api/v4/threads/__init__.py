from __future__ import annotations

import uuid
import pathlib
from typing import Any, Annotated

import litestar
from litestar.exceptions import NotFoundException
from litestar.params import Parameter
from litestar.openapi.spec import Example
from litestar.types import ControllerRouterHandler

from .models import (
    ThreadsFavoriteResponse,
    ThreadsMeResponse,
    ThreadContent,
)

ROOT_PATH = pathlib.Path(__file__).parent
DATA_PATH = ROOT_PATH / "data"


@litestar.get("/v4/threads/favorite", summary="/v4/threads/favorite")
async def v4__threads__favorite(
    *,
    limit: Annotated[int | None, Parameter(examples=[Example(value=30)])] = None,  # TODO: valid range
    token: Annotated[str, Parameter(header="authorization")],
) -> ThreadsFavoriteResponse:
    return ThreadsFavoriteResponse(items=[], next_cursor=None)


@litestar.get("/v4/threads/me", summary="/v4/threads/me")
async def v4__threads__me(
    *,
    limit: Annotated[int | None, Parameter(examples=[Example(value=30)])] = None,  # TODO: valid range
    token: Annotated[str, Parameter(header="authorization")],
) -> ThreadsMeResponse:
    return ThreadsMeResponse(items=[])


@litestar.get("/v4/threads/modules", summary="/v4/threads/modules")
async def v4__threads__modules(
    *,
    # TODO: unknown if params are required or optional, and what defaults are
    module_id: Annotated[
        uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("b91175fc-8190-4dde-8e92-01d58ed48f46"))])
    ],
    fav_talent_filter: Annotated[bool, Parameter(examples=[Example(value=False)])],
    filter_language: Annotated[str, Parameter(examples=[Example(value="en")])],
    limit: Annotated[int | None, Parameter(examples=[Example(value=5)])] = None,  # TODO: valid range
    token: Annotated[str, Parameter(header="authorization")],
) -> Any:  # FIXME: https://api.holoplus.com/v4/threads/modules?module_id=b91175fc-8190-4dde-8e92-01d58ed48f46&fav_talent_filter=false&filter_language=en&limit=5
    """NOT IMPLEMENTED"""
    ...


@litestar.get("/v4/threads/updated", summary="/v4/threads/updated")
async def v4__threads__updated(
    *,
    # TODO: unknown if params are required or optional, and what defaults are
    channel_id: Annotated[
        uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("2f495a98-f005-4ef4-b164-be922b823b42"))])
    ],
    fav_talent_filter: Annotated[bool, Parameter(examples=[Example(value=False)])],
    filter_language: Annotated[str, Parameter(examples=[Example(value="en")])],
    limit: Annotated[int | None, Parameter(examples=[Example(value=20)])] = None,  # TODO: valid range
    offset: Annotated[int | None, Parameter(examples=[Example(value=0)])] = None,  # TODO: valid range
    token: Annotated[str, Parameter(header="authorization")],
) -> Any:  # FIXME: https://api.holoplus.com/v4/threads/updated?channel_id=69efbc03-aec9-4e33-a6bd-280c36925c00&fav_talent_filter=false&filter_language=en&limit=20&offset=0
    """NOT IMPLEMENTED"""
    ...


@litestar.get(
    "/v4/threads/{thread_id:uuid}/contents", summary="/v4/threads/{thread_id:uuid}/contents", raises=[NotFoundException]
)
async def v4__threads__id__contents(
    *,
    thread_id: Annotated[
        uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("e1272fb1-38bc-4e29-aeb8-f8a9443c3340"))])
    ],
    token: Annotated[str, Parameter(header="authorization")],
) -> ThreadContent:
    return ThreadContent(
        reply_count=3,
        reaction_total=3057,
        user_reacted_count=0,
        is_favorite=False,
    )


@litestar.post(
    "/v4/threads/{thread_id:uuid}/favorite",
    summary="/v4/threads/{thread_id:uuid}/favorite",
    raises=[NotFoundException],
    status_code=201,
)
async def v4__threads__id__favorite__post(
    *,
    thread_id: Annotated[
        uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("c7186c9b-6c6d-4269-b4cf-5a2bb97acbd2"))])
    ],
    token: Annotated[str, Parameter(header="authorization")],
) -> None:
    """Returns empty response"""
    return None


@litestar.delete(
    "/v4/threads/{thread_id:uuid}/favorite",
    summary="/v4/threads/{thread_id:uuid}/favorite",
    raises=[NotFoundException],
    status_code=204,
)
async def v4__threads__id__favorite__delete(
    *,
    thread_id: Annotated[
        uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("c7186c9b-6c6d-4269-b4cf-5a2bb97acbd2"))])
    ],
    token: Annotated[str, Parameter(header="authorization")],
) -> None:
    """Returns empty response"""
    return None


ROUTES: list[ControllerRouterHandler] = [
    v4__threads__favorite,
    v4__threads__me,
    v4__threads__modules,
    v4__threads__updated,
    v4__threads__id__contents,
    v4__threads__id__favorite__post,
    v4__threads__id__favorite__delete,
]
