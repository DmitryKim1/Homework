import logging
from pathlib import Path

def setup_logging():
    Path("logs").mkdir(exist_ok=True)

    logging.basicConfig(
        filename="logs/app.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )