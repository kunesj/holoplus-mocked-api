from __future__ import annotations

import pathlib
import uuid

from holoplus_mocked_api.v5.models import Thread

ROOT_PATH = pathlib.Path(__file__).parent

THREADS: list[Thread] = [Thread.load_json(unit_path) for unit_path in (ROOT_PATH / "threads").iterdir()]
THREADS_MAP: dict[uuid.UUID, Thread] = {x.id: x for x in THREADS}
