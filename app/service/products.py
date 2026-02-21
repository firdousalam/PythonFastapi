import json
from pathlib import Path
from typing import List, Dict

DATA_FILE = Path(__file__).parent.parent / "data" / "products.json"
print(DATA_FILE)


def load_products() -> List[Dict]:
    print(DATA_FILE.exists())
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        print(file)
        return json.load(file)


def get_all_products() -> List[Dict]:
    return load_products()
