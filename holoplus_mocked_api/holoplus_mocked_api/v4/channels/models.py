from __future__ import annotations

import uuid
from typing import Annotated

import msgspec


class ChannelsIdUpdatedThreadResponse(msgspec.Struct, kw_only=True):
    channel_id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("18eec09c-ce17-4f50-bfc6-8b47457882ed")])] = (
        msgspec.field()
    )
    updated_at: Annotated[int, msgspec.Meta(examples=[1757152800])] = msgspec.field()
