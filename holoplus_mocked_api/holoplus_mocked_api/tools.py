from __future__ import annotations

from typing import Any

import msgspec


def struct_to_dict(value: msgspec.Struct) -> dict[str, Any]:
    return {f: getattr(value, f) for f in value.__struct_fields__}
