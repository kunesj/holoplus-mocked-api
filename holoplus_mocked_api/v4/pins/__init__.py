from __future__ import annotations

import uuid
from typing import Annotated

import litestar
from litestar import status_codes
from litestar.params import Parameter
from litestar.openapi.spec import Example
from litestar.types import ControllerRouterHandler

from holoplus_mocked_api.enums import FilterLanguages
from holoplus_mocked_api.exceptions import HoloplusNotFoundException


@litestar.post(
    "/v4/pins/{record_id:uuid}",
    summary="/v4/pins/{record_id:uuid}",
    raises=[HoloplusNotFoundException],
    status_code=status_codes.HTTP_204_NO_CONTENT,
)
async def v4__pins__id(
    *,
    record_id: Annotated[str, Parameter(examples=[Example(value=uuid.UUID("2f495a98-f005-4ef4-b164-be922b823b42"))])],
    filter_language: Annotated[FilterLanguages | None, Parameter(examples=[Example(value="en")])] = None,
    token: Annotated[str, Parameter(header="authorization")],
) -> None:
    """Returns empty response"""
    return None


ROUTES: list[ControllerRouterHandler] = [
    v4__pins__id,
]
