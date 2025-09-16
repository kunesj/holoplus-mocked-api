from __future__ import annotations

import uuid
from typing import Annotated

import litestar
from litestar import status_codes
from litestar.params import Body, Parameter
from litestar.openapi.spec import Example
from litestar.types import ControllerRouterHandler

from holoplus_mocked_api.exceptions import HoloplusNotFoundException

from .models import ReactionsContentsPostRequest


@litestar.post(
    "/v4/reactions/contents/{record_id:uuid}",
    summary="/v4/reactions/contents/{record_id:uuid}",
    raises=[HoloplusNotFoundException],
    status_code=status_codes.HTTP_204_NO_CONTENT,
)
async def v4__reactions__contents__id(
    data: Annotated[ReactionsContentsPostRequest, Body()],
    *,
    record_id: Annotated[str, Parameter(examples=[Example(value=uuid.UUID("b2ee47b9-2225-4c25-990a-3c6430531c8e"))])],
    token: Annotated[str, Parameter(header="authorization")],
) -> None:
    """Returns empty response"""
    return None


ROUTES: list[ControllerRouterHandler] = [
    v4__reactions__contents__id,
]
