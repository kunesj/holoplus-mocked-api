from __future__ import annotations

import uuid
from typing import Annotated

import litestar
from litestar.params import Parameter
from litestar.openapi.spec import Example
from litestar.types import ControllerRouterHandler

from holoplus_mocked_api.exceptions import HoloplusNotFoundException

from .models import Thread
from .data import THREADS_MAP


class ThreadFoundException(HoloplusNotFoundException):
    holoplus_detail = "thread not found"


@litestar.get("/v5/threads/{thread_id:uuid}", summary="/v5/threads/{thread_id:uuid}", raises=[ThreadFoundException])
async def v5__thread(
    *,
    thread_id: Annotated[
        uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("e1272fb1-38bc-4e29-aeb8-f8a9443c3340"))])
    ],
    token: Annotated[str, Parameter(header="authorization")],
) -> Thread:
    if thread_id in THREADS_MAP:
        return THREADS_MAP[thread_id]

    raise ThreadFoundException()


ROUTES: list[ControllerRouterHandler] = [litestar.Router("", tags=["/v5"], route_handlers=[v5__thread])]
