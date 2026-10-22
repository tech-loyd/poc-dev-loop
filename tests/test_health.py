"""GET /health 端点测试。

语义约定：未知查询参数一律忽略（返回 200，不影响响应），
本套件不做响应体完整字段集合断言，仅断言任务验收要求的字段。
"""
from fastapi.testclient import TestClient

from app.main import app


def test_health_returns_ok() -> None:
    """正向：GET /health 返回 200 且 status 字段为 ok。"""
    client = TestClient(app)
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"


def test_health_rejects_post() -> None:
    """负向：/health 仅接受 GET，POST 返回 405。"""
    client = TestClient(app)
    resp = client.post("/health")
    assert resp.status_code == 405


def test_health_ignores_unknown_query_params() -> None:
    """负向：未知查询参数语义为忽略，仍返回 200。"""
    client = TestClient(app)
    resp = client.get("/health", params={"unknown": "whatever"})
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"
