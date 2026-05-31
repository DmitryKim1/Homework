import unittest

from Day7.services import add_record, filter_by_category, filter_by_type
from Day7.report import total_by_type, balance, category_stats


class TestServices(unittest.TestCase):

    def setUp(self):
        self.records = [
            {
                "id": 1,
                "type": "expense",
                "amount": 100,
                "category": "food",
                "date": "2026-05-04",
                "comment": "lunch",
            },
            {
                "id": 2,
                "type": "income",
                "amount": 1000,
                "category": "salary",
                "date": "2026-05-04",
                "comment": "job",
            },
        ]

    def test_add_record(self):
        result = add_record(
            self.records,
            "expense",
            50,
            "transport",
            "2026-05-04",
            "metro"
        )

        self.assertEqual(result["id"], 3)
        self.assertEqual(len(self.records), 3)

    def test_filter_by_category(self):
        result = filter_by_category(self.records, "food")
        self.assertEqual(len(result), 1)

    def test_filter_by_type_expense(self):
        result = filter_by_type(self.records, "expense")
        self.assertEqual(len(result), 1)

    def test_total_income(self):
        result = total_by_type(self.records, "income")
        self.assertEqual(result, 1000)

    def test_total_expense(self):
        result = total_by_type(self.records, "expense")
        self.assertEqual(result, 100)

    def test_balance(self):
        result = balance(self.records)
        self.assertEqual(result, 900)

    def test_category_stats(self):
        result = category_stats(self.records)
        self.assertEqual(result["food"], 100)
        self.assertEqual(result["salary"], 1000)

    def test_wrong_type(self):
        with self.assertRaises(ValueError):
            add_record(
                self.records,
                "wrong",
                100,
                "food",
                "2026-05-04",
                ""
            )

    def test_negative_amount(self):
        with self.assertRaises(ValueError):
            add_record(
                self.records,
                "expense",
                -100,
                "food",
                "2026-05-04",
                ""
            )

    def test_wrong_date(self):
        with self.assertRaises(ValueError):
            add_record(
                self.records,
                "expense",
                100,
                "food",
                "04-05-2026",
                ""
            )


if __name__ == "__main__":
    unittest.main()