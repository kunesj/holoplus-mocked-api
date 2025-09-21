from __future__ import annotations

import pathlib
import uuid
from typing import Annotated, Self

import litestar.serialization
import msgspec


class Application(msgspec.Struct, kw_only=True):
    version: Annotated[str, msgspec.Meta(examples=["3.0.0"])] = msgspec.field()


class Agreement(msgspec.Struct, kw_only=True):
    name: Annotated[str, msgspec.Meta(examples=["privacy_policy"])] = msgspec.field()
    version: Annotated[str, msgspec.Meta(examples=["2023/08/29"])] = msgspec.field()
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("51bb7ea7-73b6-3019-9dc5-4838ad0e8bba")])] = (
        msgspec.field()
    )


class AgreementsResponse(msgspec.Struct, kw_only=True):
    items: Annotated[list[Agreement], msgspec.Meta()] = msgspec.field()

    @classmethod
    def load_json(cls, path: pathlib.Path) -> Self:
        return litestar.serialization.decode_json(path.read_bytes(), cls, strict=True)


class Talent(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("dddf28dc-0166-48c5-a845-88e608121cc0")])] = (
        msgspec.field()
    )
    name: Annotated[str, msgspec.Meta(examples=["Takanashi Kiara"])] = msgspec.field()
    key_name: Annotated[str, msgspec.Meta(examples=["takanashi_kiara"])] = msgspec.field()
    img_url: Annotated[
        str, msgspec.Meta(examples=["https://asset.holoplus.com/talents/hololive/takanashi_kiara/icon.png"])
    ] = msgspec.field()


class Icon(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("3e4026bd-50f4-451c-8c61-795a4ec815d7")])] = (
        msgspec.field()
    )
    icon_url: Annotated[
        str,
        msgspec.Meta(examples=["https://asset.holoplus.com/talents/hololive/takanashi_kiara/motif.png"]),
    ] = msgspec.field()


class Community(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("3f255c77-3b3e-4585-8e4f-7e5a4adcef58")])] = (
        msgspec.field()
    )
    name: Annotated[str, msgspec.Meta(examples=["holoplus"])] = msgspec.field()
    icon_url: Annotated[
        str, msgspec.Meta(examples=["https://asset.holoplus.com/communities/holoplus/icon_holoplus.png"])
    ] = msgspec.field()
    img_url: Annotated[str, msgspec.Meta(examples=[""])] = msgspec.field()
    is_official: Annotated[bool, msgspec.Meta(examples=[True])] = msgspec.field()
    group_id: Annotated[str, msgspec.Meta(examples=[""])] = msgspec.field()
    created_at: Annotated[int, msgspec.Meta(examples=[0])] = msgspec.field()
    updated_at: Annotated[int, msgspec.Meta(examples=[0])] = msgspec.field()


class MePushNotificationSetting(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("651c6bc3-2027-4ebe-b89a-fde71dd22905")])] = (
        msgspec.field()
    )
    sname: Annotated[str, msgspec.Meta(examples=["Official posts featuring My Oshi"])] = msgspec.field()
    created_at: Annotated[int, msgspec.Meta(examples=[0])] = msgspec.field()
    updated_at: Annotated[int, msgspec.Meta(examples=[0])] = msgspec.field()


class PushNotificationSetting(MePushNotificationSetting, kw_only=True):
    is_user_enabled: Annotated[bool, msgspec.Meta(examples=[True])] = msgspec.field()


class PushNotificationGroup(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("1027f4e8-f52b-4975-98ce-2fa38687067a")])] = (
        msgspec.field()
    )
    condition: Annotated[str, msgspec.Meta(examples=[""])] = msgspec.field()
    notification_group: Annotated[str, msgspec.Meta(examples=["Push notifications for reactions"])] = msgspec.field()
    created_at: Annotated[int, msgspec.Meta(examples=[1756796362])] = msgspec.field()
    updated_at: Annotated[int, msgspec.Meta(examples=[1756796362])] = msgspec.field()
    push_notification_settings: Annotated[list[PushNotificationSetting], msgspec.Meta()] = msgspec.field()


class PushNotificationGroupsResponse(msgspec.Struct, kw_only=True):
    items: Annotated[list[PushNotificationGroup], msgspec.Meta()] = msgspec.field()

    @classmethod
    def load_json(cls, path: pathlib.Path) -> Self:
        return litestar.serialization.decode_json(path.read_bytes(), cls, strict=True)


class Me(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta()] = msgspec.field()
    name: Annotated[str, msgspec.Meta(examples=["John Doe"])] = msgspec.field()
    onboarding: Annotated[bool, msgspec.Meta(examples=[True])] = msgspec.field()
    holoplus_point: Annotated[int, msgspec.Meta(examples=[7620])] = msgspec.field()
    level: Annotated[int, msgspec.Meta(examples=[12])] = msgspec.field()
    role: Annotated[str, msgspec.Meta(examples=["none"])] = msgspec.field()
    opt_in: Annotated[bool, msgspec.Meta(examples=[True])] = msgspec.field()
    language: Annotated[str, msgspec.Meta(examples=["en"])] = msgspec.field()
    talents: Annotated[list[Talent], msgspec.Meta()] = msgspec.field()
    icon: Annotated[Icon, msgspec.Meta()] = msgspec.field()
    communities: Annotated[list[Community], msgspec.Meta()] = msgspec.field()
    push_notification_settings: Annotated[list[MePushNotificationSetting], msgspec.Meta()] = msgspec.field()

    @classmethod
    def load_json(cls, path: pathlib.Path) -> Self:
        return litestar.serialization.decode_json(path.read_bytes(), cls, strict=True)


class MeAgreement(msgspec.Struct, kw_only=True):
    agreement: Annotated[Agreement, msgspec.Meta()] = msgspec.field()


class MeAgreementsResponse(msgspec.Struct, kw_only=True):
    items: Annotated[list[MeAgreement], msgspec.Meta()] = msgspec.field()


class MeDevice(msgspec.Struct, kw_only=True):
    id: Annotated[str, msgspec.Meta(examples=["00000b988c2b9c52"])] = msgspec.field()
    fcm_token: Annotated[str, msgspec.Meta(examples=["*****"])] = msgspec.field()
    created_at: Annotated[int, msgspec.Meta(examples=[1757169645])] = msgspec.field()
    updated_at: Annotated[int, msgspec.Meta(examples=[1757169645])] = msgspec.field()


class MePushNotificationSettingsPutRequest(msgspec.Struct, kw_only=True):
    setting_ids: Annotated[list[uuid.UUID], msgspec.Meta()] = msgspec.field()
