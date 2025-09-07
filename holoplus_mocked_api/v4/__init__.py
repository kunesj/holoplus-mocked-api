from __future__ import annotations

import uuid
import pathlib
from typing import Any, Annotated, Literal

import litestar
from litestar.exceptions import NotFoundException
from litestar.params import Body, Parameter
from litestar.openapi.spec import Example
from litestar.types import ControllerRouterHandler

from .models import ReactionsContentsPostRequest, StreamEventsResponse, StreamEvent

ROOT_PATH = pathlib.Path(__file__).parent
DATA_PATH = ROOT_PATH / "data"


@litestar.get("/v4/threads/favorite", summary="/v4/threads/favorite")
async def v4__threads__favorite(
    *,
    limit: Annotated[int | None, Parameter(examples=[Example(value=30)])] = None,  # TODO: valid range
    token: Annotated[str, Parameter(header="authorization")],
) -> Any:  # FIXME: https://api.holoplus.com/v4/threads/favorite?limit=20
    ...


@litestar.get("/v4/threads/me", summary="/v4/threads/me")
async def v4__threads__me(
    *,
    limit: Annotated[int | None, Parameter(examples=[Example(value=30)])] = None,  # TODO: valid range
    token: Annotated[str, Parameter(header="authorization")],
) -> Any:  # FIXME: https://api.holoplus.com/v4/threads/me?limit=20
    ...


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
) -> Any:  # FIXME: https://api.holoplus.com/v4/threads/e1272fb1-38bc-4e29-aeb8-f8a9443c3340/contents
    ...


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


@litestar.get("/v4/stream_events", summary="/v4/stream_events")
async def v4__stream_events(
    *,
    fav_talent_filter: Annotated[bool, Parameter(examples=[Example(value=False)])],
    plan: Annotated[Literal["past", "current", "future"], Parameter(examples=[Example(value="past")])],
    token: Annotated[str, Parameter(header="authorization")],
) -> Any:
    if plan == "past":
        return StreamEventsResponse.load_json(DATA_PATH / "stream_events__past.json")
    if plan == "current":
        return StreamEventsResponse.load_json(DATA_PATH / "stream_events__current.json")
    return StreamEventsResponse.load_json(DATA_PATH / "stream_events__future.json")


@litestar.get(
    "/v4/stream_events/{event_id:str}", summary="/v4/stream_events/{event_id:str}", raises=[NotFoundException]
)
async def v4__stream_events__id(
    *,
    event_id: Annotated[str, Parameter(examples=[Example(value="7tyO2iBAdAA")])],
    token: Annotated[str, Parameter(header="authorization")],
) -> StreamEvent:
    json_path = DATA_PATH / "stream_events" / f"{event_id}.json"
    if json_path.exists():
        return StreamEvent.load_json(json_path)
    raise NotFoundException()


@litestar.get("/v4/talent-channel/channels", summary="/v4/talent-channel/channels")
async def v4__talent_channel__channels(
    *,
    token: Annotated[str, Parameter(header="authorization")],
) -> Any:  # FIXME: https://api.holoplus.com/v4/talent-channel/channels
    ...


@litestar.get("/v4/talent-channel/threads/newest", summary="/v4/talent-channel/threads/newest")
async def v4__talent_channel__threads__newest(
    *,
    channel_id: Annotated[
        uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("7f237193-e0f7-4127-af78-9f5c255069ac"))])
    ],
    limit: Annotated[int | None, Parameter(examples=[Example(value=20)])] = None,  # TODO: valid range
    token: Annotated[str, Parameter(header="authorization")],
) -> Any:  # FIXME: https://api.holoplus.com/v4/talent-channel/threads/newest?channel_id=7f237193-e0f7-4127-af78-9f5c255069ac&limit=20
    ...


@litestar.get("/v4/talent-channel/comments/popular", summary="/v4/talent-channel/comments/popular")
async def v4__talent_channel__comments__popular(
    *,
    thread_id: Annotated[
        uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("c7186c9b-6c6d-4269-b4cf-5a2bb97acbd2"))])
    ],
    limit: Annotated[int | None, Parameter(examples=[Example(value=20)])] = None,  # TODO: valid range
    token: Annotated[str, Parameter(header="authorization")],
) -> Any:  # FIXME: https://api.holoplus.com/v4/talent-channel/comments/popular?thread_id=c7186c9b-6c6d-4269-b4cf-5a2bb97acbd2&limit=20
    ...


@litestar.get("/v4/talent-channel/comments/newest", summary="/v4/talent-channel/comments/newest")
async def v4__talent_channel__comments__newest(
    *,
    thread_id: Annotated[
        uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("c7186c9b-6c6d-4269-b4cf-5a2bb97acbd2"))])
    ],
    limit: Annotated[int | None, Parameter(examples=[Example(value=20)])] = None,  # TODO: valid range
    token: Annotated[str, Parameter(header="authorization")],
) -> Any:  # FIXME: https://api.holoplus.com/v4/talent-channel/comments/newest?thread_id=c7186c9b-6c6d-4269-b4cf-5a2bb97acbd2&limit=20
    ...


@litestar.get("/v4/comments/me", summary="/v4/comments/me")
async def v4__comments__me(
    *,
    limit: Annotated[int | None, Parameter(examples=[Example(value=20)])] = None,  # TODO: valid range
    token: Annotated[str, Parameter(header="authorization")],
) -> Any:  # FIXME: https://api.holoplus.com/v4/comments/me?limit=20
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
) -> Any:  # FIXME: https://api.holoplus.com/v4/comments/cfdd2f8b-ee45-4e3f-b4df-c150f826e224/contents
    ...


@litestar.get(
    "/v4/channels/{channel_id:uuid}/updated_thread",
    summary="/v4/channels/{channel_id:uuid}/updated_thread",
    raises=[NotFoundException],
)
async def v4__channels__id__updated_thread(
    *,
    channel_id: Annotated[str, Parameter(examples=[Example(value=uuid.UUID("18eec09c-ce17-4f50-bfc6-8b47457882ed"))])],
    filter_language: Annotated[str, Parameter(examples=[Example(value="en")])],
    token: Annotated[str, Parameter(header="authorization")],
) -> (
    Any
):  # FIXME: https://api.holoplus.com/v4/channels/18eec09c-ce17-4f50-bfc6-8b47457882ed/updated_thread?filter_language=en
    ...


@litestar.post(
    "/v4/reactions/contents/{record_id:uuid}",
    summary="/v4/reactions/contents/{record_id:uuid}",
    raises=[NotFoundException],
    status_code=204,
)
async def v4__reactions__contents__id(
    data: Annotated[ReactionsContentsPostRequest, Body()],
    *,
    record_id: Annotated[str, Parameter(examples=[Example(value=uuid.UUID("b2ee47b9-2225-4c25-990a-3c6430531c8e"))])],
    token: Annotated[str, Parameter(header="authorization")],
) -> None:
    """Returns empty response"""
    return None


@litestar.post(
    "/v4/pins/{record_id:uuid}", summary="/v4/pins/{record_id:uuid}", raises=[NotFoundException], status_code=204
)
async def v4__pins__id(
    *,
    record_id: Annotated[str, Parameter(examples=[Example(value=uuid.UUID("2f495a98-f005-4ef4-b164-be922b823b42"))])],
    filter_language: Annotated[str, Parameter(examples=[Example(value="en")])],
    token: Annotated[str, Parameter(header="authorization")],
) -> None:
    """Returns empty response"""
    return None


ROUTES: list[ControllerRouterHandler] = [
    litestar.Router(
        "",
        tags=["/v4"],
        route_handlers=[
            v4__threads__favorite,
            v4__threads__me,
            v4__threads__modules,
            v4__threads__updated,
            v4__threads__id__contents,
            v4__threads__id__favorite__post,
            v4__threads__id__favorite__delete,
            v4__stream_events,
            v4__stream_events__id,
            v4__talent_channel__channels,
            v4__talent_channel__threads__newest,
            v4__talent_channel__comments__popular,
            v4__talent_channel__comments__newest,
            v4__comments__me,
            v4__comments__popular,
            v4__comments__id__contents,
            v4__channels__id__updated_thread,
            v4__reactions__contents__id,
            v4__pins__id,
        ],
    )
]
