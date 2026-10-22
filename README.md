# poc-dev-loop — AI dev team PoC 一次性测试仓库

> 本仓库用于 ai-dev-team 平台的 GitHub 闭环验证（Issue → PR → CI → 独立验收）。
> 一次性用途，禁止放入任何真实业务数据、凭据或 HealthOS 代码。

## 首个 toy issue（对应 docs/07 P3-P7）

为 FastAPI 应用实现 `GET /health`，返回 `{"status":"ok"}`（JSON，稳定字段名）。
Developer 须附测试并开 PR；Reviewer/QA 独立跑正/负向用例并绑定 PR SHA 出结论。

## 本地运行

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
pytest -q
uvicorn app.main:app --port 8765
```
