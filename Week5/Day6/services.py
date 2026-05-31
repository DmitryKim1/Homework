def filter_by_category(records, category):
    result = []

    for record in records:
        if record["category"] == category:
            result.append(record)

    return result


def filter_by_type(records, record_type):
    result = []

    for record in records:
        if record["type"] == record_type:
            result.append(record)

    return result


def add_record(records, record_type, amount, category, date, comment=""):
    new_id = 1

    if records:
        ids = [record["id"] for record in records]
        new_id = max(ids) + 1

    record = {
        "id": new_id,
        "type": record_type,
        "amount": amount,
        "category": category,
        "date": date,
        "comment": comment,
    }

    records.append(record)
    return record