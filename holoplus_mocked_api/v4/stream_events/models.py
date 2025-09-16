from __future__ import annotations

import pathlib
import uuid
from typing import Annotated, Self

import litestar.serialization
import msgspec


class StreamEventsResponseItem(msgspec.Struct, kw_only=True):
    id: Annotated[str, msgspec.Meta(examples=["7tyO2iBAdAA"])] = msgspec.field()
    date_time: Annotated[int, msgspec.Meta(examples=[1757134803])] = msgspec.field()
    is_live: Annotated[bool, msgspec.Meta(examples=[True])] = msgspec.field()
    platform_type: Annotated[str, msgspec.Meta(examples=["youtube"])] = msgspec.field()
    url: Annotated[
        str,
        msgspec.Meta(
            examples=[
                "https://www.youtube.com/watch?utm_campaign=hp_holodule&utm_medium=social&utm_source=holoplus&v=7tyO2iBAdAA"
            ]
        ),
    ] = msgspec.field()
    thumbnail: Annotated[str, msgspec.Meta(examples=["https://img.youtube.com/vi/7tyO2iBAdAA/mqdefault.jpg"])] = (
        msgspec.field()
    )
    title: Annotated[
        str,
        msgspec.Meta(
            examples=[
                (
                    "【 逆転検事1&2 御剣セレクション #9 | 初見 】50時間連続で法廷バトルをしてしまった男、"
                    "検事になる ※ネタバレあり【 水無世燐央 l UPROAR!! 】"
                )
            ]
        ),
    ] = msgspec.field()
    reaction_total: Annotated[int, msgspec.Meta(examples=[0])] = msgspec.field()
    created_at: Annotated[int, msgspec.Meta(examples=[0])] = msgspec.field()
    updated_at: Annotated[int, msgspec.Meta(examples=[0])] = msgspec.field()


class StreamEventsResponse(msgspec.Struct, kw_only=True):
    items: Annotated[list[StreamEventsResponseItem], msgspec.Meta()] = msgspec.field()

    @classmethod
    def load_json(cls, path: pathlib.Path) -> Self:
        return litestar.serialization.decode_json(path.read_bytes(), cls, strict=True)


class StreamEventStreamer(msgspec.Struct, kw_only=True):
    id: Annotated[str, msgspec.Meta(examples=[""])] = msgspec.field()
    name: Annotated[str, msgspec.Meta(examples=["Aragami Oga"])] = msgspec.field()
    image_url: Annotated[
        str,
        msgspec.Meta(
            examples=[
                "https://yt3.ggpht.com/ytc/AIdro_no8uiFd1WlhKoZYuEgmQqu4HfEdgKbvh5NF21Tw24b4A=s88-c-k-c0x00ffffff-no-rj"
            ]
        ),
    ] = msgspec.field()
    created_at: Annotated[int | None, msgspec.Meta(examples=[None])] = msgspec.field()
    updated_at: Annotated[int | None, msgspec.Meta(examples=[None])] = msgspec.field()


class StreamEventTalent(msgspec.Struct, kw_only=True):
    id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("d464459c-758c-4c12-92cf-cb7e648a0fb8")])] = (
        msgspec.field()
    )
    name: Annotated[str, msgspec.Meta(examples=["Aragami Oga"])] = msgspec.field()
    key_name: Annotated[str, msgspec.Meta(examples=["aragami_oga"])] = msgspec.field()
    img_url: Annotated[
        str, msgspec.Meta(examples=["https://asset.holoplus.com/talents/holostars/aragami_oga/icon.png"])
    ] = msgspec.field()
    created_at: Annotated[int, msgspec.Meta(examples=[-62135596800])] = msgspec.field()
    updated_at: Annotated[int, msgspec.Meta(examples=[-62135596800])] = msgspec.field()
    deleted_at: Annotated[int | None, msgspec.Meta(examples=[None])] = msgspec.field()
    group_id: Annotated[uuid.UUID, msgspec.Meta(examples=[uuid.UUID("ff581af5-329c-490c-8156-7ee04416cd9d")])] = (
        msgspec.field()
    )


class StreamEvent(msgspec.Struct, kw_only=True):
    id: Annotated[str, msgspec.Meta(examples=["60js97Pfc6I"])] = msgspec.field()
    date_time: Annotated[int, msgspec.Meta(examples=[1757206200])] = msgspec.field()
    is_live: Annotated[bool, msgspec.Meta(examples=[False])] = msgspec.field()
    platform_type: Annotated[str, msgspec.Meta(examples=["youtube"])] = msgspec.field()
    url: Annotated[
        str,
        msgspec.Meta(
            examples=[
                "https://www.youtube.com/watch?utm_campaign=hp_holodule&utm_medium=social&utm_source=holoplus&v=60js97Pfc6I"
            ]
        ),
    ] = msgspec.field()
    thumbnail: Annotated[str, msgspec.Meta(examples=["https://img.youtube.com/vi/60js97Pfc6I/mqdefault.jpg"])] = (
        msgspec.field()
    )
    title: Annotated[
        str,
        msgspec.Meta(
            examples=[
                "【アーカイブなし】異世界転生したらドゲンジャーズだった件 9話ミラー配信【荒咬オウガ ホロスターズ】"
            ]
        ),
    ] = msgspec.field()
    reaction_total: Annotated[int, msgspec.Meta(examples=[0])] = msgspec.field()
    streamer: Annotated[StreamEventStreamer, msgspec.Meta()] = msgspec.field()
    talents: Annotated[StreamEventTalent, msgspec.Meta()] = msgspec.field()
    created_at: Annotated[int, msgspec.Meta(examples=[0])] = msgspec.field()
    updated_at: Annotated[int, msgspec.Meta(examples=[0])] = msgspec.field()

    @classmethod
    def load_json(cls, path: pathlib.Path) -> Self:
        return litestar.serialization.decode_json(path.read_bytes(), cls, strict=True)
