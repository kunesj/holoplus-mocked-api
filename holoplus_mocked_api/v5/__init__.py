from __future__ import annotations

import uuid
from typing import Annotated

import litestar
from litestar.exceptions import NotFoundException
from litestar.params import Parameter
from litestar.openapi.spec import Example
from litestar.types import ControllerRouterHandler

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

    raise NotFoundException()
    # TODO: {
    #     "code": "E100",
    #     "message": "ネットワークの状況をご確認の上、アプリの再起動などをしても改善しない場合は、「マイページ＞設定・アプリ情報＞お問い合わせ」からお問い合わせください。",
    #     "detail": "thread not found",
    #     "title": "不明なエラーが発生しました😢"
    # }


ROUTES: list[ControllerRouterHandler] = [litestar.Router("", tags=["/v5"], route_handlers=[v5__thread])]
