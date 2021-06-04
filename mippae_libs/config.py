from pathlib import Path
import os

app_dir = Path(os.path.dirname(os.path.realpath(__file__)))
SECRETKEY = os.getenv("SECRETKEY")