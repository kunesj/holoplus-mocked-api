from __future__ import annotations

import uuid
from typing import Annotated

import litestar
from litestar.exceptions import NotFoundException
from litestar.params import Parameter
from litestar.openapi.spec import Example
from litestar.types import ControllerRouterHandler

from .models import ChannelsIdUpdatedThreadResponse


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
) -> ChannelsIdUpdatedThreadResponse:
    return ChannelsIdUpdatedThreadResponse(channel_id=channel_id, updated_at=1757152800)


ROUTES: list[ControllerRouterHandler] = [
    v4__channels__id__updated_thread,
]
