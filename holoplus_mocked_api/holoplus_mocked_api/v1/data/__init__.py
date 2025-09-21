from __future__ import annotations

import pathlib

from holoplus_mocked_api.v1.models import (
    Agreement,
    AgreementsResponse,
    Community,
    Me,
    PushNotificationGroup,
    PushNotificationGroupsResponse,
)

ROOT_PATH = pathlib.Path(__file__).parent

AGREEMENTS: list[Agreement] = [*AgreementsResponse.load_json(ROOT_PATH / "agreements.json").items]
AGREEMENTS_MAP: dict[str, Agreement] = {x.name: x for x in AGREEMENTS}

PUSH_NOTIFICATION_GROUPS: list[PushNotificationGroup] = [
    *PushNotificationGroupsResponse.load_json(ROOT_PATH / "push_notification_settings.json").items
]

ME = Me.load_json(ROOT_PATH / "me.json")
