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
    TalentChannelChannelsResponse,
    TalentChannelThreadsNewestResponse,
)

ROOT_PATH = pathlib.Path(__file__).parent
DATA_PATH = ROOT_PATH / "data"


@litestar.get("/v4/talent-channel/channels", summary="/v4/talent-channel/channels")
async def v4__talent_channel__channels(
    *,
    token: Annotated[str, Parameter(header="authorization")],
) -> TalentChannelChannelsResponse:
    return TalentChannelChannelsResponse.load_json(DATA_PATH / "talent-channel__channels.json")


@litestar.get(
    "/v4/talent-channel/threads/newest", summary="/v4/talent-channel/threads/newest", raises=[NotFoundException]
)
async def v4__talent_channel__threads__newest(
    *,
    channel_id: Annotated[
        uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("7f237193-e0f7-4127-af78-9f5c255069ac"))])
    ],
    limit: Annotated[int | None, Parameter(examples=[Example(value=20)])] = None,  # TODO: valid range
    token: Annotated[str, Parameter(header="authorization")],
) -> TalentChannelThreadsNewestResponse:
    if channel_id == uuid.UUID("7f237193-e0f7-4127-af78-9f5c255069ac"):
        return TalentChannelThreadsNewestResponse.load_json(
            DATA_PATH / "talent-channel__threads__newest" / "7f237193-e0f7-4127-af78-9f5c255069ac.json"
        )
    # TODO: this is a guess
    raise NotFoundException()


@litestar.get("/v4/talent-channel/comments/popular", summary="/v4/talent-channel/comments/popular")
async def v4__talent_channel__comments__popular(
    *,
    thread_id: Annotated[
        uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("c7186c9b-6c6d-4269-b4cf-5a2bb97acbd2"))])
    ],
    limit: Annotated[int | None, Parameter(examples=[Example(value=20)])] = None,  # TODO: valid range
    token: Annotated[str, Parameter(header="authorization")],
) -> Any:  # FIXME: https://api.holoplus.com/v4/talent-channel/comments/popular?thread_id=c7186c9b-6c6d-4269-b4cf-5a2bb97acbd2&limit=20
    """NOT IMPLEMENTED"""
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
    """NOT IMPLEMENTED"""
    ...


ROUTES: list[ControllerRouterHandler] = [
    v4__talent_channel__channels,
    v4__talent_channel__threads__newest,
    v4__talent_channel__comments__popular,
    v4__talent_channel__comments__newest,
]
