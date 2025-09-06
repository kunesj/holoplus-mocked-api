from __future__ import annotations

from typing import Annotated

import litestar
import litestar.exceptions
from litestar.params import Parameter
from litestar.openapi.spec import Example

from .models import Application, AgreementList, Me, MeAgreement, MeAgreementList, PushNotificationGroupList, MeDevice
from .data import AGREEMENTS, ME, PUSH_NOTIFICATION_GROUPS


@litestar.get("/v1/agreements", summary="/v1/agreements")
async def v1__agreements() -> AgreementList:
    return AgreementList(items=[AGREEMENTS["privacy_policy"], AGREEMENTS["term"]])


@litestar.get("/v1/application", summary="/v1/application")
async def v1__application() -> Application:
    return Application(version="3.0.0")


@litestar.get("/v1/push_notification_settings", summary="/v1/push_notification_settings")
async def v1__push_notification_settings() -> PushNotificationGroupList:
    return PushNotificationGroupList(items=PUSH_NOTIFICATION_GROUPS)


@litestar.get("/v1/me", summary="/v1/me")
async def v1__me() -> Me:
    return ME


@litestar.get("/v1/me/agreements", summary="/v1/me/agreements")
async def v1__me__agreements() -> MeAgreementList:
    return MeAgreementList(
        items=[MeAgreement(agreement=AGREEMENTS["privacy_policy"]), MeAgreement(agreement=AGREEMENTS["term"])]
    )


@litestar.get("/v1/me/push_notification_settings", summary="/v1/me/push_notification_settings")
async def v1__me__push_notification_settings() -> Me:
    return ME


@litestar.get("/v1/me/devices/{device_id:str}", summary="/v1/me/devices/{device_id:str}")
async def v1__me__devices(
    device_id: Annotated[str, Parameter(examples=[Example(value="94131b988c2b9c52")])],
) -> MeDevice:
    return MeDevice(
        id=device_id,
        fcm_token="*****",
        created_at=1757169645,
        updated_at=1757169645,
    )


ROUTES: list[litestar.handlers.HTTPRouteHandler] = [
    v1__agreements,
    v1__application,
    v1__push_notification_settings,
    v1__me,
    v1__me__agreements,
    v1__me__push_notification_settings,
    v1__me__devices,
]
