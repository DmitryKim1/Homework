import argparse

from storage import load_records, save_records
from services import add_record, filter_by_category, filter_by_type
from report import total_by_type, balance, category_stats


def show_records(records):
    if not records:
        print("Записей пока нет")
        return

    for record in records:
        print(
            f'{record["id"]}. '
            f'{record["type"]} | '
            f'{record["amount"]} | '
            f'{record["category"]} | '
            f'{record["date"]} | '
            f'{record["comment"]}'
        )


def command_add(args):
    records = load_records()

    record = add_record(
        records,
        args.type,
        args.amount,
        args.category,
        args.date,
        args.comment
    )

    save_records(records)
    print(f"Запись добавлена: {record}")


def command_list(args):
    records = load_records()

    if args.category:
        records = filter_by_category(records, args.category)

    if args.type:
        records = filter_by_type(records, args.type)

    show_records(records)


def command_stats(args):
    records = load_records()

    income = total_by_type(records, "income")
    expense = total_by_type(records, "expense")
    current_balance = balance(records)
    stats = category_stats(records)

    print(f"Доходы: {income}")
    print(f"Расходы: {expense}")
    print(f"Баланс: {current_balance}")
    print("По категориям:")

    for category, total in stats.items():
        print(f"{category}: {total}")


def build_parser():
    parser = argparse.ArgumentParser(description="Трекер расходов и доходов")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("type", choices=["income", "expense"])
    add_parser.add_argument("amount", type=float)
    add_parser.add_argument("category")
    add_parser.add_argument("date")
    add_parser.add_argument("--comment", default="")
    add_parser.set_defaults(func=command_add)

    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("--category")
    list_parser.add_argument("--type", choices=["income", "expense"])
    list_parser.set_defaults(func=command_list)

    stats_parser = subparsers.add_parser("stats")
    stats_parser.set_defaults(func=command_stats)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    args.func(args)


if __name__ == "__main__":
    main()