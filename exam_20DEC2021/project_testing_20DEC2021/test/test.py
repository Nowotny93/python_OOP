from python_oop_exams.project_testing_20DEC2021.movie import Movie

import unittest


class PetShopTests(unittest.TestCase):

    def setUp(self):
        self.m = Movie('Harry', 2001, 3.50)

    def test_init(self):
        self.assertEqual('Harry', self.m.name)
        self.assertEqual(2001, self.m.year)
        self.assertEqual(3.50, self.m.rating)
        self.assertEqual([], self.m.actors)

    def test_invalid_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.m.name = ''
        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test_invalid_year_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.m.year = 1665
        self.assertEqual("Year is not valid!", str(ex.exception))

    def test_adding_non_existing_actor(self):
        self.m.actors = ['Peter', 'John']
        self.m.add_actor('Liza')
        self.assertEqual(['Peter', 'John', 'Liza'], self.m.actors)

    def test_adding_existing_actor(self):
        self.m.actors = ['Peter', 'John']
        res = self.m.add_actor('Peter')
        self.assertEqual("Peter is already added in the list of actors!", res)

    def test_gt_method_first_time(self):
        movie1 = Movie("FirstMovie", 2005, 7.50)
        movie2 = Movie("SecondMovie", 2006, 8.80)
        movie1.rating = 7.50
        movie2.rating = 8.80
        self.assertTrue('"SecondMovie" is better than "FirstMovie"')

    def test_gt_method_second_time(self):
        movie1 = Movie("FirstMovie", 2005, 9.50)
        movie2 = Movie("SecondMovie", 2006, 8.80)
        movie1.rating = 9.50
        movie2.rating = 8.80
        self.assertTrue('"FirstMovie" is better than "SecondMovie"')

    def test_repr_method(self):
        self.m.actors = ['Peter', 'John']
        self.assertEqual(f"Name: Harry\n"
                         f"Year of Release: 2001\n"
                         f"Rating: 3.50\n"
                         f"Cast: Peter, John", str(self.m))
        # actual_result = self.m.__repr__()
        # expected_result = f"Name: {self.m.name}\n" \
        # f"Year of Release: {self.m.year}\n" \
        # f"Rating: {self.m.rating:.2f}\n" \
        # f"Cast: {', '.join(self.m.actors)}"
        # self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
