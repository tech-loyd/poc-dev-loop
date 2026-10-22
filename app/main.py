"""poc-dev-loop 空壳应用。

/health 端点故意缺失：由 Developer agent 在 toy issue 中实现（见仓库 README）。
"""
from fastapi import FastAPI

app = FastAPI(title="poc-dev-loop")


@app.get("/")
def root() -> dict:
    """冒烟端点：仅证明应用可启动。"""
    return {"repo": "poc-dev-loop", "purpose": "ai-dev-team PoC"}


@app.get("/health")
def health() -> dict:
    """存活探测端点。"""
    return {"status": "ok", "service": "poc"}
