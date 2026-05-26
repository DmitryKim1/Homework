import argparse
import logging

from storage import load_transactions, save_transactions, export_json
from services import (
    add_transaction,
    filter_transactions,
    get_total_by_type,
    get_balance,
    get_category_stats,
    build_report,
)

DATA_FILE = "transactions.csv"

def print_transaction(transaction):
    print(
        f'{transaction["id"]}. '
        f'{transaction["type"]} | '
        f'{transaction["amount"]} | '
        f'{transaction["category"]} | '
        f'{transaction["date"]} | '
        f'{transaction["comment"]}'
    )

def handle_add(args):
    transactions = load_transactions(DATA_FILE)

    transaction = add_transaction(
        transactions=transactions,
        transaction_type=args.type,
        amount=args.amount,
        category=args.category,
        date=args.date,
        comment=args.comment,
    )

    save_transactions(transactions, DATA_FILE)

    logging.info(f"Added transaction: {transaction}")

    print("Транзакция добавлена:")
    print_transaction(transaction)

def handle_list(args):
    transactions = load_transactions(DATA_FILE)

    filtered = filter_transactions(
        transactions,
        transaction_type=args.type,
        category=args.category,
    )

    if not filtered:
        print("Транзакций нет")
        return
    
    for transaction in filtered:
        print_transaction(transaction)

    logging.info("Listed transactions")

def handle_stats(args):
    transactions = load_transactions(DATA_FILE)

    income = get_total_by_type(transactions, "income")
    expense = get_total_by_type(transactions, "expense")
    balance = get_balance(transactions)
    category_stats = get_category_stats(transactions)

    print("Доходы:", income)
    print("Расходы", expense)
    print("Баланс", balance)
    print("Расходы по категориям: ", category_stats)

    logging.info("Showed stats")

def handle_export(args):
    transactions = load_transactions(DATA_FILE)

    if args.format == "json":
        report = build_report(transactions)
        export_json(report, args.output)
        print(f"Отчет сохранен: {args.output}")
        logging.info(f"Exported report to {args.output}")

    elif args.format == "csv":
        save_transactions(transactions, args.output)
        print(f"CSV сохранен: {args.output}")
        logging.info(f"Exported CSV to {args.output}")

def build_parser():
    parser = argparse.ArgumentParser(
        description="CLI трекер расходов и доходов"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    add_parser = subparsers.add_parser(
        "add",
        help="Добавить транзакцию",
    )

    add_parser.add_argument("--type", required=True, choices=["income", "expense"])
    add_parser.add_argument("--amount", required=True, type=int)
    add_parser.add_argument("--category", required=True)
    add_parser.add_argument("--date", required=True)
    add_parser.add_argument("--comment", default="")
    add_parser.set_defaults(func=handle_add)

    list_parser = subparsers.add_parser(
        "list",
        help="Показать транзакции",
    )
    list_parser.add_argument("--type", choices=["income", "expense"])
    list_parser.add_argument("--category")
    list_parser.set_defaults(func=handle_list)

    stats_parser = subparsers.add_parser(
        "stats",
        help="Показать статистику",
    )
    stats_parser.set_defaults(func=handle_stats)

    export_parser = subparsers.add_parser(
        "export",
        help="Экспорт отчета",
    )
    export_parser.add_argument("--format", required=True, choices=["json", "csv"])
    export_parser.add_argument("--output", required=True)
    export_parser.set_defaults(func=handle_export)

    return parser