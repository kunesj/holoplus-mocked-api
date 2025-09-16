from __future__ import annotations

import litestar
import litestar.openapi
from litestar.exceptions import HTTPException

from .exceptions import exception_handler, litestar_monkey_patch
from .googleapis_com import ROUTES as GOOGLEAPIS_COM_ROUTES
from .v1 import ROUTES as V1_ROUTES
from .v2 import ROUTES as V2_ROUTES
from .v3 import ROUTES as V3_ROUTES
from .v4 import ROUTES as V4_ROUTES
from .v5 import ROUTES as V5_ROUTES


def create_app() -> litestar.Litestar:
    litestar_monkey_patch()
    return litestar.Litestar(
        route_handlers=[*GOOGLEAPIS_COM_ROUTES, *V1_ROUTES, *V2_ROUTES, *V3_ROUTES, *V4_ROUTES, *V5_ROUTES],
        openapi_config=litestar.openapi.OpenAPIConfig(
            title="Holoplus API (Mocked)",
            version="3.0.0",
            use_handler_docstrings=True,
        ),
        exception_handlers={
            Exception: exception_handler,
            HTTPException: exception_handler,
        },
    )
