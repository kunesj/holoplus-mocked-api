from __future__ import annotations

from typing import Annotated

import msgspec


class ReactionsContentsPostRequest(msgspec.Struct, kw_only=True):
    reaction_count: Annotated[int, msgspec.Meta(examples=[1])] = msgspec.field()
    target_type: Annotated[str, msgspec.Meta(examples=["comment"])] = msgspec.field()
