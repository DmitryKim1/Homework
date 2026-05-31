def total_by_type(records, record_type):
    total = 0

    for record in records:
        if record["type"] == record_type:
            total += record["amount"]

    return total


def balance(records):
    income = total_by_type(records, "income")
    expense = total_by_type(records, "expense")

    return income - expense


def category_stats(records):
    stats = {}

    for record in records:
        category = record["category"]

        if category not in stats:
            stats[category] = 0

        stats[category] += record["amount"]

    return stats