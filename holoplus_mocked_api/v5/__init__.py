from __future__ import annotations

import uuid
from typing import Annotated

import litestar
from litestar.exceptions import NotFoundException
from litestar.params import Parameter
from litestar.openapi.spec import Example

from .models import Thread
from .data import THREADS_MAP


@litestar.get("/v5/threads/{thread_id:uuid}", summary="/v5/threads/{thread_id:uuid}", raises=[NotFoundException])
async def v5__thread(
    *,
    thread_id: Annotated[
        uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("e1272fb1-38bc-4e29-aeb8-f8a9443c3340"))])
    ],
    token: Annotated[str, Parameter(header="authorization")],
) -> Thread:
    if thread_id in THREADS_MAP:
        return THREADS_MAP[thread_id]
    # TODO: this is a guess
    raise NotFoundException()


ROUTES: list[litestar.handlers.HTTPRouteHandler] = [v5__thread]
