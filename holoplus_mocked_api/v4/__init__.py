from __future__ import annotations

import litestar
from litestar.types import ControllerRouterHandler

from .threads import ROUTES as THREADS_ROUTES
from .stream_events import ROUTES as STREAM_EVENTS_ROUTES
from .talent_channel import ROUTES as TALENT_CHANNEL_ROUTES
from .comments import ROUTES as COMMENTS_ROUTES
from .channels import ROUTES as CHANNELS_ROUTES
from .reactions import ROUTES as REACTIONS_ROUTES
from .pins import ROUTES as PINS_ROUTES


ROUTES: list[ControllerRouterHandler] = [
    litestar.Router(
        "",
        tags=["/v4"],
        route_handlers=[
            *THREADS_ROUTES,
            *STREAM_EVENTS_ROUTES,
            *TALENT_CHANNEL_ROUTES,
            *COMMENTS_ROUTES,
            *CHANNELS_ROUTES,
            *REACTIONS_ROUTES,
            *PINS_ROUTES,
        ],
    )
]
