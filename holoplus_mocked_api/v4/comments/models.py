from __future__ import annotations

from typing import Annotated

import msgspec
from litestar.openapi.spec import Example
from litestar.params import Parameter


class CommentContent(msgspec.Struct, kw_only=True):
    comment_total: Annotated[int, Parameter(examples=[Example(value=0)])] = msgspec.field()
    reaction_total: Annotated[int, Parameter(examples=[Example(value=6)])] = msgspec.field()
    user_reacted_count: Annotated[int, Parameter(examples=[Example(value=0)])] = msgspec.field()
