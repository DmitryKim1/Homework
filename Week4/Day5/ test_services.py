import unittest
from services import LibraryService

class TestLibraryService(unittest.TestCase):

    def setUp(self):
        self.service = LibraryService()

    def test_add_book(self):
        book = self.service.add_book("1984", "Orwell")

        self.assertEqual(book.title, "1984")
        self.assertEqual(book.author, "Orwell")
        self.assertEqual(book.status, "planned")
        self.assertEqual(len(self.service.books), 1)

    def test_add_book_empty_title(self):
        with self.assertRaises(ValueError):
            self.service.add_book("", "Orwell")
    
    def test_find_book_not_found(self):
        with self.assertRaises(ValueError):
            self.service.find_by_id(999)

    def test_find_by_id(self):
        self.service.add_book("1984", "Orwell")

        book = self.service.find_by_id(1)

        self.assertEqual(book.id, 1)
        self.assertEqual(book.title, "1984")

    def test_mark_as_read(self):
        self.service.add_book("1984", "Orwell")

        result = self.service.mark_as_read(1)

        self.assertTrue(result)
        self.assertEqual(self.service.books[0].status, "read")

if __name__ == "__main__":
    unittest.main()