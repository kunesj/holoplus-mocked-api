from __future__ import annotations

import uuid
from typing import Annotated, Any

import litestar
from litestar.exceptions import NotFoundException
from litestar.params import Parameter
from litestar.openapi.spec import Example
from litestar.types import ControllerRouterHandler

from .models import CommentContent


@litestar.get("/v4/comments/me", summary="/v4/comments/me")
async def v4__comments__me(
    *,
    limit: Annotated[int | None, Parameter(examples=[Example(value=20)])] = None,  # TODO: valid range
    token: Annotated[str, Parameter(header="authorization")],
) -> Any:  # FIXME: https://api.holoplus.com/v4/comments/me?limit=20
    """NOT IMPLEMENTED"""
    ...


@litestar.get("/v4/comments/popular", summary="/v4/comments/popular")
async def v4__comments__popular(
    *,
    thread_id: Annotated[
        uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("a4d526d1-2c97-476f-ae12-849fdef41eb8"))])
    ],
    limit: Annotated[int | None, Parameter(examples=[Example(value=20)])] = None,  # TODO: valid range
    filter_language: Annotated[str, Parameter(examples=[Example(value="en")])],
    token: Annotated[str, Parameter(header="authorization")],
) -> Any:  # FIXME: https://api.holoplus.com/v4/comments/popular?thread_id=a4d526d1-2c97-476f-ae12-849fdef41eb8&limit=20&filter_language=en
    """NOT IMPLEMENTED"""
    ...


@litestar.get(
    "/v4/comments/{comment_id:uuid}/contents",
    summary="/v4/comments/{comment_id:uuid}/contents",
    raises=[NotFoundException],
)
async def v4__comments__id__contents(
    *,
    comment_id: Annotated[str, Parameter(examples=[Example(value=uuid.UUID("cfdd2f8b-ee45-4e3f-b4df-c150f826e224"))])],
    token: Annotated[str, Parameter(header="authorization")],
) -> CommentContent:
    return CommentContent(
        comment_total=0,
        reaction_total=6,
        user_reacted_count=0,
    )


ROUTES: list[ControllerRouterHandler] = [
    v4__comments__me,
    v4__comments__popular,
    v4__comments__id__contents,
]
