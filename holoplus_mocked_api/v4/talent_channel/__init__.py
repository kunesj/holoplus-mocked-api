from __future__ import annotations

import uuid
import pathlib
from typing import Annotated

import litestar
from litestar.params import Parameter
from litestar.openapi.spec import Example
from litestar.types import ControllerRouterHandler

from holoplus_mocked_api.exceptions import HoloplusNotFoundException

from .models import (
    TalentChannelChannelsResponse,
    TalentChannelCommentsResponse,
    TalentChannelThreadsResponse,
)

ROOT_PATH = pathlib.Path(__file__).parent
DATA_PATH = ROOT_PATH / "data"


class TalentNotFoundException(HoloplusNotFoundException):
    holoplus_detail = "failed to get talents: talent not found"


@litestar.get("/v4/talent-channel/channels", summary="/v4/talent-channel/channels")
async def v4__talent_channel__channels(
    *,
    token: Annotated[str, Parameter(header="authorization")],
) -> TalentChannelChannelsResponse:
    return TalentChannelChannelsResponse.load_json(DATA_PATH / "talent-channel__channels.json")


@litestar.get(
    "/v4/talent-channel/threads/newest", summary="/v4/talent-channel/threads/newest", raises=[TalentNotFoundException]
)
async def v4__talent_channel__threads__newest(
    *,
    channel_id: Annotated[
        uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("7f237193-e0f7-4127-af78-9f5c255069ac"))])
    ],
    limit: Annotated[int | None, Parameter(examples=[Example(value=20)], ge=1, le=30)] = None,
    token: Annotated[str, Parameter(header="authorization")],
) -> TalentChannelThreadsResponse:
    if channel_id == uuid.UUID("7f237193-e0f7-4127-af78-9f5c255069ac"):
        return TalentChannelThreadsResponse.load_json(
            DATA_PATH / "talent-channel__threads__newest" / "7f237193-e0f7-4127-af78-9f5c255069ac.json"
        )
    raise TalentNotFoundException()


@litestar.get("/v4/talent-channel/comments/popular", summary="/v4/talent-channel/comments/popular")
async def v4__talent_channel__comments__popular(
    *,
    thread_id: Annotated[
        uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("c7186c9b-6c6d-4269-b4cf-5a2bb97acbd2"))])
    ],
    limit: Annotated[int | None, Parameter(examples=[Example(value=20)], ge=1, le=30)] = None,
    token: Annotated[str, Parameter(header="authorization")],
) -> TalentChannelCommentsResponse:
    json_path = DATA_PATH / "talent-channel__comments__popular" / f"{thread_id}.json"
    if json_path.exists():
        return TalentChannelCommentsResponse.load_json(json_path)

    return TalentChannelCommentsResponse(items=[])


@litestar.get("/v4/talent-channel/comments/newest", summary="/v4/talent-channel/comments/newest")
async def v4__talent_channel__comments__newest(
    *,
    thread_id: Annotated[
        uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("c7186c9b-6c6d-4269-b4cf-5a2bb97acbd2"))])
    ],
    limit: Annotated[int | None, Parameter(examples=[Example(value=20)], ge=1, le=30)] = None,
    token: Annotated[str, Parameter(header="authorization")],
) -> TalentChannelCommentsResponse:
    json_path = DATA_PATH / "talent-channel__comments__newest" / f"{thread_id}.json"
    if json_path.exists():
        return TalentChannelCommentsResponse.load_json(json_path)

    return TalentChannelCommentsResponse(items=[])


ROUTES: list[ControllerRouterHandler] = [
    v4__talent_channel__channels,
    v4__talent_channel__threads__newest,
    v4__talent_channel__comments__popular,
    v4__talent_channel__comments__newest,
]
