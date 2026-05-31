from pathlib import Path
from storage import (
    read_transactions_csv,
    iter_transactions_csv,
    save_transactions_json,
    load_transactions_json,
    save_transactions_csv,
    find_csv_files,
    get_category_stats,
    save_category_report_json,
)

def main():
    BASE_DIR = Path(__file__).resolve().parent
    csv_file = BASE_DIR / "transactions.csv"
    json_file = BASE_DIR / "report.json"
    report_file = "output/category_report.json"
    export_csv_file = "output/export.csv"

    print("1. Читаем csv полностью")
    transactions = read_transactions_csv(csv_file)
    print(transactions)

    print()
    print("2. Читаем csv построчно через генератор")
    for transaction in iter_transactions_csv(csv_file):
        print(transaction)

    print()
    print("3. Сохраняем транзакции в json")
    save_transactions_json(transactions, json_file)

    print()
    print("4. Загружаем транзакции из json")
    loaded = load_transactions_json(json_file)
    print(loaded)

    print()
    print("5. Сохраняем транзакции обратно в csv")
    save_transactions_csv(transactions, export_csv_file)

    print()
    print("6. Ищем csv файлы в папке data")
    csv_files = find_csv_files("data")
    print(csv_files)

    print()
    print("7. Статистика по категориям")
    stats = get_category_stats(transactions)
    print(stats)

    print()
    print("8. Сохраняем отчет по категориям в json")
    save_category_report_json(transactions, report_file)

if __name__ == "__main__":
    main()