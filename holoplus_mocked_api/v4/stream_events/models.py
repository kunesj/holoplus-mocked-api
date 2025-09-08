from __future__ import annotations

import pathlib
import uuid
from typing import Annotated, Self

import litestar.serialization
import msgspec
from litestar.openapi.spec import Example
from litestar.params import Parameter


class StreamEventsResponseItem(msgspec.Struct, kw_only=True):
    id: Annotated[str, Parameter(examples=[Example(value="7tyO2iBAdAA")])] = msgspec.field()
    date_time: Annotated[int, Parameter(examples=[Example(value=1757134803)])] = msgspec.field()
    is_live: Annotated[bool, Parameter(examples=[Example(value=True)])] = msgspec.field()
    platform_type: Annotated[str, Parameter(examples=[Example(value="youtube")])] = msgspec.field()
    url: Annotated[
        str,
        Parameter(
            examples=[
                Example(
                    value="https://www.youtube.com/watch?utm_campaign=hp_holodule&utm_medium=social&utm_source=holoplus&v=7tyO2iBAdAA"
                )
            ]
        ),
    ] = msgspec.field()
    thumbnail: Annotated[
        str, Parameter(examples=[Example(value="https://img.youtube.com/vi/7tyO2iBAdAA/mqdefault.jpg")])
    ] = msgspec.field()
    title: Annotated[
        str,
        Parameter(
            examples=[
                Example(
                    value=(
                        "【 逆転検事1&2 御剣セレクション #9 | 初見 】50時間連続で法廷バトルをしてしまった男、"
                        "検事になる ※ネタバレあり【 水無世燐央 l UPROAR!! 】"
                    )
                )
            ]
        ),
    ] = msgspec.field()
    reaction_total: Annotated[int, Parameter(examples=[Example(value=0)])] = msgspec.field()
    created_at: Annotated[int, Parameter(examples=[Example(value=0)])] = msgspec.field()
    updated_at: Annotated[int, Parameter(examples=[Example(value=0)])] = msgspec.field()


class StreamEventsResponse(msgspec.Struct, kw_only=True):
    items: Annotated[list[StreamEventsResponseItem], Parameter()] = msgspec.field()

    @classmethod
    def load_json(cls, path: pathlib.Path) -> Self:
        return litestar.serialization.decode_json(path.read_bytes(), cls, strict=True)


class StreamEventStreamer(msgspec.Struct, kw_only=True):
    id: Annotated[str, Parameter(examples=[Example(value="")])] = msgspec.field()
    name: Annotated[str, Parameter(examples=[Example(value="Aragami Oga")])] = msgspec.field()
    image_url: Annotated[
        str,
        Parameter(
            examples=[
                Example(
                    value="https://yt3.ggpht.com/ytc/AIdro_no8uiFd1WlhKoZYuEgmQqu4HfEdgKbvh5NF21Tw24b4A=s88-c-k-c0x00ffffff-no-rj"
                )
            ]
        ),
    ] = msgspec.field()
    created_at: Annotated[int | None, Parameter(examples=[Example(value=None)])] = msgspec.field()
    updated_at: Annotated[int | None, Parameter(examples=[Example(value=None)])] = msgspec.field()


class StreamEventTalent(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("d464459c-758c-4c12-92cf-cb7e648a0fb8"))])] = (
        msgspec.field()
    )
    name: Annotated[str, Parameter(examples=[Example(value="Aragami Oga")])] = msgspec.field()
    key_name: Annotated[str, Parameter(examples=[Example(value="aragami_oga")])] = msgspec.field()
    img_url: Annotated[
        str, Parameter(examples=[Example(value="https://asset.holoplus.com/talents/holostars/aragami_oga/icon.png")])
    ] = msgspec.field()
    created_at: Annotated[int, Parameter(examples=[Example(value=-62135596800)])] = msgspec.field()
    updated_at: Annotated[int, Parameter(examples=[Example(value=-62135596800)])] = msgspec.field()
    deleted_at: Annotated[int | None, Parameter(examples=[Example(value=None)])] = msgspec.field()
    group_id: Annotated[
        uuid.UUID, Parameter(examples=[Example(value=uuid.UUID("ff581af5-329c-490c-8156-7ee04416cd9d"))])
    ] = msgspec.field()


class StreamEvent(msgspec.Struct, kw_only=True):
    id: Annotated[str, Parameter(examples=[Example(value="60js97Pfc6I")])] = msgspec.field()
    date_time: Annotated[int, Parameter(examples=[Example(value=1757206200)])] = msgspec.field()
    is_live: Annotated[bool, Parameter(examples=[Example(value=False)])] = msgspec.field()
    platform_type: Annotated[str, Parameter(examples=[Example(value="youtube")])] = msgspec.field()
    url: Annotated[
        str,
        Parameter(
            examples=[
                Example(
                    value="https://www.youtube.com/watch?utm_campaign=hp_holodule&utm_medium=social&utm_source=holoplus&v=60js97Pfc6I"
                )
            ]
        ),
    ] = msgspec.field()
    thumbnail: Annotated[
        str, Parameter(examples=[Example(value="https://img.youtube.com/vi/60js97Pfc6I/mqdefault.jpg")])
    ] = msgspec.field()
    title: Annotated[
        str,
        Parameter(
            examples=[
                Example(
                    value=(
                        "【アーカイブなし】異世界転生したらドゲンジャーズだった件 "
                        "9話ミラー配信【荒咬オウガ ホロスターズ】"
                    )
                )
            ]
        ),
    ] = msgspec.field()
    reaction_total: Annotated[int, Parameter(examples=[Example(value=0)])] = msgspec.field()
    streamer: Annotated[StreamEventStreamer, Parameter()] = msgspec.field()
    talents: Annotated[StreamEventTalent, Parameter()] = msgspec.field()
    created_at: Annotated[int, Parameter(examples=[Example(value=0)])] = msgspec.field()
    updated_at: Annotated[int, Parameter(examples=[Example(value=0)])] = msgspec.field()

    @classmethod
    def load_json(cls, path: pathlib.Path) -> Self:
        return litestar.serialization.decode_json(path.read_bytes(), cls, strict=True)
