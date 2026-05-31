from Day7.validators import validate_type, validate_amount, validate_date


def get_next_id(records):
    if not records:
        return 1

    ids = [record["id"] for record in records]
    return max(ids) + 1


def add_record(records, record_type, amount, category, date, comment=""):
    validate_type(record_type)
    validate_amount(amount)
    validate_date(date)

    record = {
        "id": get_next_id(records),
        "type": record_type,
        "amount": amount,
        "category": category,
        "date": date,
        "comment": comment,
    }

    records.append(record)
    return record


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