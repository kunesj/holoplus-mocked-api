from __future__ import annotations

import itertools
import pathlib
import uuid

from holoplus_mocked_api.v2.models import (
    Banner,
    Channel,
    Group,
    Module,
    Unit,
    V2Community,
    V2CommunitiesResponse,
    BannersResponse,
    ModulesResponse,
)

ROOT_PATH = pathlib.Path(__file__).parent

_communities_response = V2CommunitiesResponse.load_json(ROOT_PATH / "me__communities.json")
COMMUNITIES: list[V2Community] = [x.community for x in _communities_response.items]
COMMUNITIES_MAP: dict[str, V2Community] = {x.name: x for x in COMMUNITIES}

CHANNELS: list[Channel] = [*itertools.chain(*[community.channels for community in COMMUNITIES])]
CHANNELS_MAP: dict[uuid.UUID, Channel] = {x.id: x for x in CHANNELS}

_banners_response = BannersResponse.load_json(ROOT_PATH / "banners.json")
BANNERS: list[Banner] = [*_banners_response.top, *_banners_response.middle]
BANNERS_MAP: dict[uuid.UUID, Banner] = {x.id: x for x in BANNERS}

MODULES: list[Module] = [*ModulesResponse.load_json(ROOT_PATH / "modules.json").items]
MODULES_MAP: dict[uuid.UUID, Module] = {x.id: x for x in MODULES}

GROUPS: list[Group] = [Group.load_json(group_path) for group_path in (ROOT_PATH / "groups").iterdir()]
GROUPS_MAP: dict[uuid.UUID, Group] = {x.id: x for x in GROUPS}

UNITS: list[Unit] = [Unit.load_json(unit_path) for unit_path in (ROOT_PATH / "units").iterdir()]
UNITS_MAP: dict[uuid.UUID, Unit] = {x.id: x for x in UNITS}
