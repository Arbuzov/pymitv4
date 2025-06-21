import sys
from pathlib import Path

# Ensure src directory is on path for tests
SRC_DIR = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC_DIR))
