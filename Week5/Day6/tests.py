import unittest

from Day6.services import filter_by_category, filter_by_type, add_record
from Day6.validators import validate_amount, validate_type
from Day6.report import total_by_type, balance

class TestDay6(unittest.TestCase):

    def setUp(self):
        self.records = [
            {
                "id": 1,
                "type": "expense",
                "amount": 100,
                "category": "food",
                "date": "2026-05-01",
                "comment": "lunch",
            },
            {
                "id": 2,
                "type": "income",
                "amount": 1000,
                "category": "salary",
                "date": "2026-05-02",
                "comment": "job",
            },
            {
                "id": 3,
                "type": "expense",
                "amount": 50,
                "category": "food",
                "date": "2026-05-03",
                "comment": "coffee",
            }
        ]
    
    def test_filter_by_category(self):
        result = filter_by_category(self.records, "food")
        self.assertEqual(len(result), 2)

    def test_filter_by_type_income(self):
        result = filter_by_type(self.records, "income")
        self.assertEqual(len(result), 1)

    def test_filter_by_type_expense(self):
        result = filter_by_type(self.records, "expense")
        self.assertEqual(len(result), 2)

    def test_add_record(self):
        result = add_record(
            self.records,
            "expense",
            200,
            "transport",
            "2026-05-03",
            "metro"
        )

        self.assertEqual(result["id"], 4)
        self.assertEqual(len(self.records), 4)

    def test_total_income(self):
        result = total_by_type(self.records, "income")
        self.assertEqual(result, 1000)

    def test_total_expense(self):
        result = total_by_type(self.records, "expense")
        self.assertEqual(result, 150)

    def test_balance(self):
        result = balance(self.records)
        self.assertEqual(result, 850)

    def test_validate_amount_error(self):
        with self.assertRaises(ValueError):
            validate_amount(-100)

    def test_add_record_empty_list(self):
        records = []

        result = add_record(
            records,
            "expense",
            100,
            "food",
            "2026-05-04",
            "lunch"
        )

        self.assertEqual(len(records), 1)
        self.assertEqual(result["id"], 1)
        self.assertEqual(result["type"], "expense")
    
if __name__ == "__main__":
    unittest.main()