from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def isolated_activities():
    original_activities = deepcopy(activities)
    yield activities
    activities.clear()
    activities.update(original_activities)


@pytest.fixture
def client(isolated_activities):
    return TestClient(app)
