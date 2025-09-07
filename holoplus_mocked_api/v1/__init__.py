from __future__ import annotations

from typing import Annotated

import litestar
from litestar.exceptions import NotFoundException
from litestar.params import Body, Parameter
from litestar.openapi.spec import Example

from .models import (
    Application,
    AgreementsResponse,
    Me,
    MeAgreement,
    MeAgreementsResponse,
    PushNotificationGroupsResponse,
    MePushNotificationSettingsPutRequest,
    MeDevice,
)
from .data import AGREEMENTS_MAP, ME, PUSH_NOTIFICATION_GROUPS


@litestar.get("/v1/agreements", summary="/v1/agreements")
async def v1__agreements(
    *,
    token: Annotated[str, Parameter(header="authorization")],
) -> AgreementsResponse:
    return AgreementsResponse(items=[AGREEMENTS_MAP["privacy_policy"], AGREEMENTS_MAP["term"]])


@litestar.get("/v1/application", summary="/v1/application")
async def v1__application() -> Application:
    """
    Doesn't need Authorization header.
    """
    return Application(version="3.0.0")


@litestar.get("/v1/push_notification_settings", summary="/v1/push_notification_settings")
async def v1__push_notification_settings(
    *,
    token: Annotated[str, Parameter(header="authorization")],
) -> PushNotificationGroupsResponse:
    return PushNotificationGroupsResponse(items=PUSH_NOTIFICATION_GROUPS)


@litestar.get("/v1/me", summary="/v1/me")
async def v1__me(
    *,
    token: Annotated[str, Parameter(header="authorization")],
) -> Me:
    return ME


@litestar.get("/v1/me/agreements", summary="/v1/me/agreements")
async def v1__me__agreements(
    *,
    token: Annotated[str, Parameter(header="authorization")],
) -> MeAgreementsResponse:
    return MeAgreementsResponse(
        items=[MeAgreement(agreement=AGREEMENTS_MAP["privacy_policy"]), MeAgreement(agreement=AGREEMENTS_MAP["term"])]
    )


@litestar.put("/v1/me/push_notification_settings", summary="/v1/me/push_notification_settings")
async def v1__me__push_notification_settings(
    data: Annotated[MePushNotificationSettingsPutRequest, Body()],
    *,
    token: Annotated[str, Parameter(header="authorization")],
) -> Me:
    return ME


@litestar.put("/v1/me/devices/{device_id:str}", summary="/v1/me/devices/{device_id:str}", raises=[NotFoundException])
async def v1__me__devices(
    *,
    device_id: Annotated[str, Parameter(examples=[Example(value="94131b988c2b9c52")])],
    fcm_registration_token: Annotated[str, Parameter(header="fcm-registration-token")],
    token: Annotated[str, Parameter(header="authorization")],
) -> MeDevice:
    return MeDevice(
        id=device_id,
        fcm_token=fcm_registration_token,
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
