from pathlib import Path
import csv
import json

def ensure_dir(path):
    path = Path(path)
    path.mkdir(parents= True, exist_ok=True)

def parse_transaction(row):
    try:
        transaction_type = row["type"].strip()
        amount = int(row["amount"])
        category = row["category"].strip()
        date = row["date"].strip()
        comment = row["comment"].strip()
    except (KeyError, ValueError, AttributeError):
        return None
    
    if transaction_type not in ["income", "expense"]:
        return None
    
    if not category or not date:
        return None
    
    return {
        "type": transaction_type,
        "amount": amount,
        "category": category,
        "date": date,
        "comment": comment,
    }

def read_transactions_csv(filename):
    transactions = []

    with open(filename, "r", encodingg = "utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            transaction = parse_transaction(row)

            if transaction is not None:
                transactions.append(transaction)
    
    return transactions

def iter_transactions_csv(filename):
    with open(filename, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            transaction = parse_transaction(row)

            if transaction is not None:
                yield transaction

def save_transactions_json(transactions, filename):
    filename = Path(filename)
    ensure_dir(filename.parent)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(transactions, file, ensure_ascii=False, indent=4)

def load_transactions_json(filename):
    filename = Path(filename)

    if not filename.exists():
        return []
    
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
    
def save_transactions_csv(transactions, filename):
    filename = Path(filename)
    ensure_dir(filename.parent)

    fieldnames = ["type", "amount", "category", "date", "comment"]

    with open(filename, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(transactions)

def find_csv_files(folder):
    folder = Path(folder)
    return list(folder.glob("*.csv"))

def get_category_stats(transactions):
    stats = {}

    for transaction in transactions:
        if transaction["type"] == "expense":
            category = transaction["category"]
            amount = transaction["amount"]

            if category not in stats:
                stats[category] = 0

            stats[category] += amount

    return stats

def save_category_report_json(transactions, filename):
    stats = get_category_stats(transactions)
    save_transactions_json(stats, filename)