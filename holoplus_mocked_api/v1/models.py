from __future__ import annotations

import pathlib
import uuid
from typing import Annotated, Self

import litestar.serialization
import msgspec
from litestar.openapi.spec import Example
from litestar.params import Parameter


class Application(msgspec.Struct, kw_only=True, omit_defaults=True):
    version: Annotated[str, Parameter(examples=[Example(value="3.0.0")])] = msgspec.field()


class Agreement(msgspec.Struct, kw_only=True, omit_defaults=True):
    name: Annotated[str, Parameter(examples=[Example(value="privacy_policy")])] = msgspec.field()
    version: Annotated[str, Parameter(examples=[Example(value="2023/08/29")])] = msgspec.field()
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("51bb7ea7-73b6-3019-9dc5-4838ad0e8bba"))])] = (
        msgspec.field()
    )


class AgreementsResponse(msgspec.Struct, kw_only=True, omit_defaults=True):
    items: Annotated[list[Agreement], Parameter()] = msgspec.field()

    @classmethod
    def load_json(cls, path: pathlib.Path) -> Self:
        return litestar.serialization.decode_json(path.read_bytes(), cls, strict=True)


class Talent(msgspec.Struct, kw_only=True, omit_defaults=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("dddf28dc-0166-48c5-a845-88e608121cc0"))])] = (
        msgspec.field()
    )
    name: Annotated[str, Parameter(examples=[Example(value="Takanashi Kiara")])] = msgspec.field()
    key_name: Annotated[str, Parameter(examples=[Example(value="takanashi_kiara")])] = msgspec.field()
    img_url: Annotated[
        str, Parameter(examples=[Example(value="https://asset.holoplus.com/talents/hololive/takanashi_kiara/icon.png")])
    ] = msgspec.field()


class Icon(msgspec.Struct, kw_only=True, omit_defaults=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("3e4026bd-50f4-451c-8c61-795a4ec815d7"))])] = (
        msgspec.field()
    )
    icon_url: Annotated[
        str,
        Parameter(examples=[Example(value="https://asset.holoplus.com/talents/hololive/takanashi_kiara/motif.png")]),
    ] = msgspec.field()


class Community(msgspec.Struct, kw_only=True, omit_defaults=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("3f255c77-3b3e-4585-8e4f-7e5a4adcef58"))])] = (
        msgspec.field()
    )
    name: Annotated[str, Parameter(examples=[Example(value="holoplus")])] = msgspec.field()
    icon_url: Annotated[
        str, Parameter(examples=[Example(value="https://asset.holoplus.com/communities/holoplus/icon_holoplus.png")])
    ] = msgspec.field()
    img_url: Annotated[str, Parameter(examples=[Example(value="")])] = msgspec.field()
    is_official: Annotated[bool, Parameter(examples=[Example(value=True)])] = msgspec.field()
    group_id: Annotated[str, Parameter(examples=[Example(value="")])] = msgspec.field()
    created_at: Annotated[int, Parameter(examples=[Example(value=0)])] = msgspec.field()
    updated_at: Annotated[int, Parameter(examples=[Example(value=0)])] = msgspec.field()


class MePushNotificationSetting(msgspec.Struct, kw_only=True, omit_defaults=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("651c6bc3-2027-4ebe-b89a-fde71dd22905"))])] = (
        msgspec.field()
    )
    sname: Annotated[str, Parameter(examples=[Example(value="Official posts featuring My Oshi")])] = msgspec.field()
    created_at: Annotated[int, Parameter(examples=[Example(value=0)])] = msgspec.field()
    updated_at: Annotated[int, Parameter(examples=[Example(value=0)])] = msgspec.field()


class PushNotificationSetting(MePushNotificationSetting, kw_only=True, omit_defaults=True):
    is_user_enabled: Annotated[bool, Parameter(examples=[Example(value=True)])] = msgspec.field()


class PushNotificationGroup(msgspec.Struct, kw_only=True, omit_defaults=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("1027f4e8-f52b-4975-98ce-2fa38687067a"))])] = (
        msgspec.field()
    )
    condition: Annotated[str, Parameter(examples=[Example(value="")])] = msgspec.field()
    notification_group: Annotated[str, Parameter(examples=[Example(value="Push notifications for reactions")])] = (
        msgspec.field()
    )
    created_at: Annotated[int, Parameter(examples=[Example(value=1756796362)])] = msgspec.field()
    updated_at: Annotated[int, Parameter(examples=[Example(value=1756796362)])] = msgspec.field()
    push_notification_settings: Annotated[list[PushNotificationSetting], Parameter()] = msgspec.field()


class PushNotificationGroupsResponse(msgspec.Struct, kw_only=True, omit_defaults=True):
    items: Annotated[list[PushNotificationGroup], Parameter()] = msgspec.field()

    @classmethod
    def load_json(cls, path: pathlib.Path) -> Self:
        return litestar.serialization.decode_json(path.read_bytes(), cls, strict=True)


class Me(msgspec.Struct, kw_only=True, omit_defaults=True):
    id: Annotated[uuid.UUID, Parameter()] = msgspec.field()
    name: Annotated[str, Parameter(examples=[Example(value="John Doe")])] = msgspec.field()
    onboarding: Annotated[bool, Parameter(examples=[Example(value=True)])] = msgspec.field()
    holoplus_point: Annotated[int, Parameter(examples=[Example(value=7620)])] = msgspec.field()
    level: Annotated[int, Parameter(examples=[Example(value=12)])] = msgspec.field()
    role: Annotated[str, Parameter(examples=[Example(value="none")])] = msgspec.field()
    opt_in: Annotated[bool, Parameter(examples=[Example(value=True)])] = msgspec.field()
    language: Annotated[str, Parameter(examples=[Example(value="en")])] = msgspec.field()
    talents: Annotated[list[Talent], Parameter()] = msgspec.field()
    icon: Annotated[Icon, Parameter()] = msgspec.field()
    communities: Annotated[list[Community], Parameter()] = msgspec.field()
    push_notification_settings: Annotated[list[MePushNotificationSetting], Parameter()] = msgspec.field()

    @classmethod
    def load_json(cls, path: pathlib.Path) -> Self:
        return litestar.serialization.decode_json(path.read_bytes(), cls, strict=True)


class MeAgreement(msgspec.Struct, kw_only=True, omit_defaults=True):
    agreement: Annotated[Agreement, Parameter()] = msgspec.field()


class MeAgreementsResponse(msgspec.Struct, kw_only=True, omit_defaults=True):
    items: Annotated[list[MeAgreement], Parameter()] = msgspec.field()


class MeDevice(msgspec.Struct, kw_only=True, omit_defaults=True):
    id: Annotated[str, Parameter(examples=[Example(value="00000b988c2b9c52")])] = msgspec.field()
    fcm_token: Annotated[str, Parameter(examples=[Example(value="*****")])] = msgspec.field()
    created_at: Annotated[int, Parameter(examples=[Example(value=1757169645)])] = msgspec.field()
    updated_at: Annotated[int, Parameter(examples=[Example(value=1757169645)])] = msgspec.field()


class MePushNotificationSettingsPutRequest(msgspec.Struct, kw_only=True, omit_defaults=True):
    setting_ids: Annotated[list[uuid.UUID], Parameter()] = msgspec.field()
