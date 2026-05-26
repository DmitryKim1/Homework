from pathlib import Path
import csv
import json

FIELDNAMES = ["id", "type", "amount", "category", "date", "comment"]

def ensure_parent(filename):
    filename = Path(filename)
    filename.parent.mkdir(parents=True, exist_ok=True)

def load_transactions(filename):
    filename = Path(filename)

    if not filename.exists():
        return []
    
    transactions = []

    with open(filename, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                transaction = {
                    "id": int(row["id"]),
                    "type": row["type"],
                    "amount": int(row["amount"]),
                    "category": row["category"],
                    "date": row["date"],
                    "comment": row["comment"],
                }
                transactions.append(transaction)
            except (KeyError, ValueError):
                continue

        return transactions
    
def save_transactions(transactions, filename):
    ensure_parent(filename)

    with open(filename, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(transactions)

def export_json(data, filename):
    ensure_parent(filename)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)