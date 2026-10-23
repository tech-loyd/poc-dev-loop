"""让 pytest（无论以 pytest 还是 python -m pytest 调用）都能导入仓库根下的 app 包。"""
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
