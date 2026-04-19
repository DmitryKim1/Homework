import unittest
from services import LibraryService

class TestLibraryService(unittest.TestCase):
    def setUp(self):
        self.service = LibraryService()

    def test_add_book(self):
        book = self.service.add_book("1984", "Orwell", "Dystopia")

        self.assertEqual(len(self.service.books), 1)
        self.assertEqual(book.title, "1984")
        self.assertEqual(book.author, "Orwell")
        self.assertEqual(book.genre, "Dystopia")
        self.assertEqual(book.status, "planned")

    def test_change_status(self):
        book = self.service.add_book("1984", "Orwell", "Dystopia")
        result = self.service.change_status(book.id, "read")

        self.assertTrue(result)
        self.assertEqual(book.status, "read")

    def test_delete_book(self):
        book = self.service.add_book("1984", "Orwell", "Dystopia")
        result = self.service.delete_book(book.id)

        self.assertTrue(result)
        self.assertEqual(len(self.service.books), 0)

    def test_search_books(self):
        self.service.add_book("1984", "Orwell", "Dystopia")
        self.service.add_book("Animal Farm", "Orwell", "Satire")

        result = self.service.search_books("orwell")

        self.assertEqual(len(result), 2)

    def test_find_by_id(self):
        book = self.service.add_book("1984", "Orwell", "Dystopia")
        found_book = self.service.find_by_id(book.id)

        self.assertEqual(found_book, book)

if __name__ == "__main__":
    unittest.main()