from python_oop_exams.project_15AUG2021 import Library

import unittest


class LibraryTests(unittest.TestCase):

    def setUp(self):

        self.l = Library('Harry')

    def test_init_(self):
        self.assertEqual('Harry', self.l.name)
        self.assertEqual({}, self.l.books_by_authors)
        self.assertEqual({}, self.l.readers)

    def test_if_name_is_empty_string_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.l.name = ''
        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_correct_name(self):
        self.l.name = 'Boby'
        self.assertEqual('Boby', self.l.name)

    def test_add_non_existing_author_and_book(self):
        self.l.books_by_authors = {'vazov': ['pod igoto'], 'botev': ['maice si']}
        self.l.add_book('debelqnov', 'nevermore')
        self.assertEqual({'vazov': ['pod igoto'], 'botev': ['maice si'], 'debelqnov': ['nevermore']},
                         self.l.books_by_authors)

    def test_add_existing_author_and_non_existing_book(self):
        self.l.books_by_authors = {'vazov': ['pod igoto'], 'botev': ['maice si']}
        self.l.add_book('botev', 'o shipka')
        self.assertEqual({'vazov': ['pod igoto'], 'botev': ['maice si', 'o shipka']}, self.l.books_by_authors)

    def test_add_existing_author_and_existing_book(self):
        self.l.books_by_authors = {'vazov': ['pod igoto'], 'botev': ['maice si']}
        self.l.add_book('botev', 'maice si')
        self.assertEqual({'vazov': ['pod igoto'], 'botev': ['maice si']}, self.l.books_by_authors)

    def test_add_non_existing_reader(self):
        self.l.readers = {'pesho': [], 'gosho': []}
        self.l.add_reader('valio')
        self.assertEqual({'pesho': [], 'gosho': [], 'valio': []}, self.l.readers)

    def test_add_existing_reader(self):
        self.l.readers = {'pesho': [], 'gosho': []}
        res = self.l.add_reader('gosho')
        self.assertEqual('gosho is already registered in the Harry library.', res)

    def test_rent_book_to_non_existing_reader(self):
        self.l.readers = {'pesho': [], 'gosho': []}
        res = self.l.rent_book('vili', 'vazov', 'pod igoto')
        self.assertEqual('vili is not registered in the Harry Library.', res)

    def test_rent_book_with_non_existing_author(self):
        self.l.readers = {'pesho': [], 'gosho': [], 'vili': []}
        self.l.books_by_authors = {'vazov': ['pod igoto'], 'botev': ['maice si']}
        res = self.l.rent_book('vili', 'slaveikov', 'samoten grob')
        self.assertEqual("Harry Library does not have any slaveikov's books.", res)

    def test_rent_book_with_non_existing_title(self):
        self.l.readers = {'pesho': [], 'gosho': [], 'vili': []}
        self.l.books_by_authors = {'vazov': ['pod igoto'], 'botev': ['maice si']}
        res = self.l.rent_book('pesho', 'botev', 'o shipka')
        self.assertEqual("""Harry Library does not have botev's "o shipka".""", res)

    def test_rent_book_successfully(self):
        self.l.readers = {'pesho': [], 'gosho': [], 'vili': []}
        self.l.books_by_authors = {'vazov': ['pod igoto'], 'botev': ['maice si']}
        self.l.rent_book('pesho', 'botev', 'maice si')
        self.assertEqual({'pesho': [{'botev': 'maice si'}], 'gosho': [], 'vili': []}, self.l.readers)

    def test_book_indexing(self):
        self.l.books_by_authors = {'vazov': ['pod igoto'], 'botev': ['maice si']}
        self.l.rent_book('pesho', 'botev', 'maice si')
        res = self.l.books_by_authors['botev'].index('maice si')
        self.assertEqual(0, res)

    def test_deleting_book_by_index(self):
        self.l.books_by_authors = {'vazov': ['pod igoto'], 'botev': ['maice si']}
        self.l.rent_book('pesho', 'botev', 'maice si')
        index_book = self.l.books_by_authors['botev'].index('maice si')
        self.assertTrue(index_book not in self.l.books_by_authors['botev'])


if __name__ == "__main__":
    unittest.main()
