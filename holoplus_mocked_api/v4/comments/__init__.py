from __future__ import annotations

import uuid
import pathlib
from typing import Annotated

import litestar
from litestar.exceptions import NotFoundException
from litestar.params import Parameter
from litestar.openapi.spec import Example
from litestar.types import ControllerRouterHandler

from .models import CommentContent, CommentsMeResponse, CommentsResponse

ROOT_PATH = pathlib.Path(__file__).parent
DATA_PATH = ROOT_PATH / "data"


@litestar.get("/v4/comments/me", summary="/v4/comments/me")
async def v4__comments__me(
    *,
    limit: Annotated[int | None, Parameter(examples=[Example(value=20)], ge=1, le=30)] = None,
    token: Annotated[str, Parameter(header="authorization")],
) -> CommentsMeResponse:
    return CommentsMeResponse.load_json(DATA_PATH / "comments__me.json")


@litestar.get("/v4/comments/popular", summary="/v4/comments/popular")
async def v4__comments__popular(
    *,
    thread_id: Annotated[
        uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("a4d526d1-2c97-476f-ae12-849fdef41eb8"))])
    ],
    limit: Annotated[int | None, Parameter(examples=[Example(value=20)], ge=1, le=30)] = None,
    filter_language: Annotated[str, Parameter(examples=[Example(value="en")])],
    token: Annotated[str, Parameter(header="authorization")],
) -> CommentsResponse:
    json_path = DATA_PATH / f"comments__popular__{thread_id}.json"
    if json_path.exists():
        return CommentsResponse.load_json(json_path)
    raise NotFoundException()


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
