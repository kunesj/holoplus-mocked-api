from __future__ import annotations

import uuid
from typing import Annotated

import msgspec
from litestar.openapi.spec import Example
from litestar.params import Parameter


class ChannelsIdUpdatedThreadResponse(msgspec.Struct, kw_only=True, omit_defaults=True):
    channel_id: Annotated[
        uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("18eec09c-ce17-4f50-bfc6-8b47457882ed"))])
    ] = msgspec.field()
    updated_at: Annotated[int, Parameter(examples=[Example(value=1757152800)])] = msgspec.field()
