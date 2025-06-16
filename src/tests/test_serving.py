import sys
from pathlib import Path
import importlib
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

fastapi_spec = importlib.util.find_spec('fastapi')
httpx_spec = importlib.util.find_spec('httpx')

pytestmark = pytest.mark.skipif(
    fastapi_spec is None or httpx_spec is None,
    reason='fastapi or httpx missing'
)

if fastapi_spec and httpx_spec:
    from fastapi.testclient import TestClient
    from src.serving.main import app
    client = TestClient(app)


def test_predict() -> None:
    if not (fastapi_spec and httpx_spec):
        pytest.skip('fastapi or httpx missing')
    response = client.post("/predict", json={"store": 1, "sku": 2})
    assert response.status_code == 200
    assert "prediction" in response.json()
