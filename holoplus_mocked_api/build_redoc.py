from __future__ import annotations

import logging

from litestar.testing import TestClient

from .app import create_app

if __name__ == "__main__":
    logging.getLogger("httpx").setLevel(logging.ERROR)

    with TestClient(app=create_app()) as client:
        response = client.get("/schema")
        print(response.text)  # noqa: T201
