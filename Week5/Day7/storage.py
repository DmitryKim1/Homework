import json
from pathlib import Path

DATA_FILE = Path("data") / "records.json"

def load_records():
    if not DATA_FILE.exists():
        return []
    
    with open(DATA_FILE, "r", encoding = "utf-8") as file:
        return json.load(file)
    
def save_records(records):
    DATA_FILE.parent.mkdir(exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(records,file, ensure_ascii=False, indent=4)