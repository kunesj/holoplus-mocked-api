from __future__ import annotations

from typing import Annotated

import msgspec
from litestar.openapi.spec import Example
from litestar.params import Parameter


class ReactionsContentsPostRequest(msgspec.Struct, kw_only=True, omit_defaults=True):
    reaction_count: Annotated[int, Parameter(examples=[Example(value=1)])] = msgspec.field()
    target_type: Annotated[str, Parameter(examples=[Example(value="comment")])] = msgspec.field()
