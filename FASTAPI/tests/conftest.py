from typing import Generator

import pytest
from fastapi.testclient import TestClient


@pytest.fixture(scope="module")
def client():
    print(12345)
    # with TestClient(app) as c:
    #     yield c
