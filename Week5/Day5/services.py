from datetime import datetime


def validate_type(transaction_type):
    if transaction_type not in ["income", "expense"]:
        raise ValueError("Тип должен быть income или expense")


def validate_amount(amount):
    if amount <= 0:
        raise ValueError("Сумма должна быть больше 0")


def validate_category(category):
    if not category.strip():
        raise ValueError("Категория не может быть пустой")


def validate_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Дата должна быть в формате YYYY-MM-DD")


def get_next_id(transactions):
    if not transactions:
        return 1

    return max(transaction["id"] for transaction in transactions) + 1


def add_transaction(transactions, transaction_type, amount, category, date, comment=""):
    validate_type(transaction_type)
    validate_amount(amount)
    validate_category(category)
    validate_date(date)

    transaction = {
        "id": get_next_id(transactions),
        "type": transaction_type,
        "amount": amount,
        "category": category.strip().lower(),
        "date": date,
        "comment": comment.strip(),
    }

    transactions.append(transaction)
    return transaction


def filter_transactions(transactions, transaction_type=None, category=None):
    result = []

    for transaction in transactions:
        if transaction_type is not None and transaction["type"] != transaction_type:
            continue

        if category is not None and transaction["category"] != category:
            continue

        result.append(transaction)

    return result


def get_total_by_type(transactions, transaction_type):
    total = 0

    for transaction in transactions:
        if transaction["type"] == transaction_type:
            total += transaction["amount"]

    return total


def get_balance(transactions):
    income = get_total_by_type(transactions, "income")
    expense = get_total_by_type(transactions, "expense")

    return income - expense


def get_category_stats(transactions):
    stats = {}

    for transaction in transactions:
        if transaction["type"] == "expense":
            category = transaction["category"]

            if category not in stats:
                stats[category] = 0

            stats[category] += transaction["amount"]

    return stats


def build_report(transactions):
    return {
        "income": get_total_by_type(transactions, "income"),
        "expense": get_total_by_type(transactions, "expense"),
        "balance": get_balance(transactions),
        "category_stats": get_category_stats(transactions),
    }