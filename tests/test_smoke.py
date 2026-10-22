"""冒烟测试：空壳应用可导入、根端点可用。/health 由后续 PR 实现。"""
from fastapi.testclient import TestClient

from app.main import app


def test_app_boots() -> None:
    client = TestClient(app)
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json()["repo"] == "poc-dev-loop"
