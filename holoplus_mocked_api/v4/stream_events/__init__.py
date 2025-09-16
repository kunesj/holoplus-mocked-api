from __future__ import annotations

import pathlib
from typing import Annotated, Literal

import litestar
from litestar.params import Parameter
from litestar.openapi.spec import Example
from litestar.types import ControllerRouterHandler

from holoplus_mocked_api.exceptions import HoloplusNotFoundException

from .models import (
    StreamEventsResponse,
    StreamEvent,
)

ROOT_PATH = pathlib.Path(__file__).parent
DATA_PATH = ROOT_PATH / "data"


@litestar.get("/v4/stream_events", summary="/v4/stream_events")
async def v4__stream_events(
    *,
    fav_talent_filter: Annotated[bool, Parameter(examples=[Example(value=False)])],
    plan: Annotated[Literal["past", "current", "future"], Parameter(examples=[Example(value="past")])],
    token: Annotated[str, Parameter(header="authorization")],
) -> StreamEventsResponse:
    if plan == "past":
        return StreamEventsResponse.load_json(DATA_PATH / "stream_events__past.json")
    if plan == "current":
        return StreamEventsResponse.load_json(DATA_PATH / "stream_events__current.json")
    return StreamEventsResponse.load_json(DATA_PATH / "stream_events__future.json")


@litestar.get(
    "/v4/stream_events/{event_id:str}", summary="/v4/stream_events/{event_id:str}", raises=[HoloplusNotFoundException]
)
async def v4__stream_events__id(
    *,
    event_id: Annotated[str, Parameter(examples=[Example(value="7tyO2iBAdAA")])],
    token: Annotated[str, Parameter(header="authorization")],
) -> StreamEvent:
    json_path = DATA_PATH / "stream_events" / f"{event_id}.json"
    if json_path.exists():
        return StreamEvent.load_json(json_path)
    raise HoloplusNotFoundException()


ROUTES: list[ControllerRouterHandler] = [
    v4__stream_events,
    v4__stream_events__id,
]
