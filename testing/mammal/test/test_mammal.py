from python_testing.mammal.project.mammal import Mammal
import unittest

class MammalTests(unittest.TestCase):

    def setUp(self):

        self.mammal = Mammal('Test', 'dragon', 'rghh')

    def test_mammal_is_initialised_correctly(self):

        self.assertEqual("Test", self.mammal.name)
        self.assertEqual('dragon', self.mammal.type)
        self.assertEqual('rghh', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_get_info(self):

        actual_result = self.mammal.info()
        expected_result = 'Test is of type dragon'
        self.assertEqual(expected_result, actual_result)

    def test_get_sound(self):

        actual_result = self.mammal.make_sound()
        expected_result = 'Test makes rghh'
        self.assertEqual(expected_result, actual_result)

    def test_get_kingdom(self):
        actual_result = self.mammal.get_kingdom()
        expected_result = self.mammal._Mammal__kingdom
        self.assertEqual(expected_result, actual_result)

if __name__ == "__main__":
    unittest.main()