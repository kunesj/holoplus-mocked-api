from __future__ import annotations

import itertools
import uuid

from holoplus_mocked_api.tools import struct_to_dict

from .models import (
    Agreement,
    Community,
    Icon,
    Me,
    MePushNotificationSetting,
    PushNotificationGroup,
    PushNotificationSetting,
    Talent,
)

AGREEMENTS: dict[str, Agreement] = {
    "privacy_policy": Agreement(
        name="privacy_policy",
        version="2023/08/29",
        id=uuid.UUID("51bb7ea7-73b6-3019-9dc5-4838ad0e8bba"),
    ),
    "term": Agreement(
        name="term",
        version="2025/08/06",
        id=uuid.UUID("962eb3a8-2b7e-e240-2225-b0d0d7f1b283"),
    ),
}
TALENTS: dict[str, Talent] = {
    "kureiji_ollie": Talent(
        id=uuid.UUID("17492aaf-a9bc-48e1-b00c-eeaeefa6b5b0"),
        name="Kureiji Ollie",
        key_name="kureiji_ollie",
        img_url="https://asset.holoplus.com/talents/hololive/kureiji_ollie/icon_20240918.png",
    ),
    "takanashi_kiara": Talent(
        id=uuid.UUID("dddf28dc-0166-48c5-a845-88e608121cc0"),
        name="Takanashi Kiara",
        key_name="takanashi_kiara",
        img_url="https://asset.holoplus.com/talents/hololive/takanashi_kiara/icon.png",
    ),
}
ICONS: dict[str, Icon] = {
    "takanashi_kiara": Icon(
        id=uuid.UUID("3e4026bd-50f4-451c-8c61-795a4ec815d7"),
        icon_url="https://asset.holoplus.com/talents/hololive/takanashi_kiara/motif.png",
    )
}
COMMUNITIES: dict[str, Community] = {
    "holoplus": Community(
        id=uuid.UUID("3f255c77-3b3e-4585-8e4f-7e5a4adcef58"),
        name="holoplus",
        icon_url="https://asset.holoplus.com/communities/holoplus/icon_holoplus.png",
        img_url="",
        is_official=True,
        group_id="",
        created_at=0,
        updated_at=0,
    ),
    "HOLOSTARS": Community(
        id=uuid.UUID("b98aa4c3-e351-45f3-bb0b-8aa037d3a750"),
        name="HOLOSTARS",
        icon_url="https://asset.holoplus.com/communities/holostars/icon_holostars.png",
        img_url="https://asset.holoplus.com/communities/holostars/myoshi_holostars_act.png",
        is_official=True,
        group_id=uuid.UUID("ff581af5-329c-490c-8156-7ee04416cd9d"),
        created_at=0,
        updated_at=0,
    ),
    "hololive": Community(
        id=uuid.UUID("f30a0c54-73c0-46c1-b413-9e3af0f672ff"),
        name="hololive",
        icon_url="https://asset.holoplus.com/communities/hololive/icon_hololive.png",
        img_url="https://asset.holoplus.com/communities/hololive/myoshi_hololive_act_0519.png",
        is_official=True,
        group_id=uuid.UUID("e9171551-cb2a-483e-8a77-fdffba8e632b"),
        created_at=0,
        updated_at=0,
    ),
}
PUSH_NOTIFICATION_GROUPS: list[PushNotificationGroup] = [
    PushNotificationGroup(
        condition="",
        id=uuid.UUID("1027f4e8-f52b-4975-98ce-2fa38687067a"),
        notification_group="Push notifications for reactions",
        created_at=1756796362,
        updated_at=1756796362,
        push_notification_settings=[
            PushNotificationSetting(
                id=uuid.UUID("f7e82c45-9a3d-4b8e-87f1-3c6d5e4a2b8f"),
                sname="Posts from My Oshi",
                created_at=0,
                updated_at=0,
                is_user_enabled=True,
            ),
            PushNotificationSetting(
                id=uuid.UUID("06bfdbb1-ec5e-4101-a1c9-cb71caeaf809"),
                sname="Posts from official accounts",
                created_at=0,
                updated_at=0,
                is_user_enabled=False,
            ),
            PushNotificationSetting(
                id=uuid.UUID("651c6bc3-2027-4ebe-b89a-fde71dd22905"),
                sname="Official posts featuring My Oshi",
                created_at=0,
                updated_at=0,
                is_user_enabled=True,
            ),
        ],
    ),
    PushNotificationGroup(
        condition="",
        id=uuid.UUID("026d75ce-046c-4b0c-9bfc-2c72560b7b1d"),
        notification_group="Push notifications for posts",
        created_at=1756796362,
        updated_at=1756796362,
        push_notification_settings=[
            PushNotificationSetting(
                id=uuid.UUID("9cb1752e-91e2-4fd0-a9d1-abaf2400e1f8"),
                sname="New reactions on your post",
                created_at=0,
                updated_at=0,
                is_user_enabled=True,
            ),
            PushNotificationSetting(
                id=uuid.UUID("f99e590e-c0b5-4d46-b0f3-8fdd2570fa07"),
                sname="New replies on your comments",
                created_at=0,
                updated_at=0,
                is_user_enabled=True,
            ),
        ],
    ),
    PushNotificationGroup(
        condition="",
        id=uuid.UUID("1d649530-003b-4a07-9f11-be2a44a156bc"),
        notification_group="Notification language for official accounts",
        created_at=1756796362,
        updated_at=1756796362,
        push_notification_settings=[
            PushNotificationSetting(
                id=uuid.UUID("e267b929-9b05-4eb1-a276-c1153e72d5df"),
                sname="日本語",
                created_at=0,
                updated_at=0,
                is_user_enabled=False,
            ),
            PushNotificationSetting(
                id=uuid.UUID("6688cb21-ed92-41da-bf2a-8bc375afe21e"),
                sname="English",
                created_at=0,
                updated_at=0,
                is_user_enabled=True,
            ),
        ],
    ),
]
PUSH_NOTIFICATION_SETTINGS: list[PushNotificationSetting] = [
    *itertools.chain(*[group.push_notification_settings for group in PUSH_NOTIFICATION_GROUPS]),
    PushNotificationSetting(
        id=uuid.UUID("a1558bf6-dcf8-de03-baf3-1e9c6f2236aa"),
        sname="New posts from official fan club accounts",
        created_at=0,
        updated_at=0,
        is_user_enabled=True,
    ),
]
ME = Me(
    id=uuid.uuid4(),
    name="John Doe",
    onboarding=True,
    holoplus_point=7620,
    level=12,
    role="none",
    opt_in=True,
    language="en",
    talents=[TALENTS["kureiji_ollie"], TALENTS["takanashi_kiara"]],
    icon=ICONS["takanashi_kiara"],
    communities=[
        COMMUNITIES["holoplus"],
        COMMUNITIES["HOLOSTARS"],
        COMMUNITIES["hololive"],
    ],
    push_notification_settings=[
        MePushNotificationSetting(**{k: v for k, v in struct_to_dict(x).items() if k != "is_user_enabled"})
        for x in PUSH_NOTIFICATION_SETTINGS
        if x.is_user_enabled
    ],
)
