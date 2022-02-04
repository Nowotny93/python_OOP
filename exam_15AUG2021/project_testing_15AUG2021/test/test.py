from python_oop_exams.project_testing_15AUG2021 import PetShop

import unittest

class PetShopTests(unittest.TestCase):

    def setUp(self):

        self.s = PetShop('Harry')

    def test_init(self):

        self.assertEqual('Harry', self.s.name)
        self.assertEqual({}, self.s.food)
        self.assertEqual([], self.s.pets)

    def test_invalid_food_quantity_zero_raises(self):

        with self.assertRaises(ValueError) as ex:
            self.s.add_food('sirene', 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_invalid_food_quantity_negative_raises(self):

        with self.assertRaises(ValueError) as ex:
            self.s.add_food('sirene', -1)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_new_food(self):

        self.s.food = {}
        res = self.s.add_food('domat', 350.50)
        self.assertEqual("Successfully added 350.50 grams of domat.", res)
        self.assertEqual({'domat': 350.50}, self.s.food)

    def test_add_existing_food(self):

        self.s.food = {'domat': 350.50}
        res = self.s.add_food('domat', 10.60)
        self.assertEqual("Successfully added 10.60 grams of domat.", res)
        self.assertEqual({'domat': 361.10}, self.s.food)

    def test_new_pet(self):

        self.s.pets = []
        res = self.s.add_pet('jojo')
        self.assertEqual("Successfully added jojo.", res)
        self.assertEqual(['jojo'], self.s.pets)

    def test_existing_pet_raises(self):

        self.s.pets = ['jojo']
        with self.assertRaises(Exception) as ex:
            self.s.add_pet('jojo')
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))
        self.assertEqual(['jojo'], self.s.pets)

    def test_feed_non_existing_pet_raises(self):

        self.s.pets = ['jojo']
        with self.assertRaises(Exception) as ex:
            self.s.feed_pet('domat', 'reksi')
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_with_non_existing_food(self):

        self.s.food = {'domat': 350.50}
        self.s.pets = ['reksi']
        res = self.s.feed_pet('krastavica', 'reksi')
        self.assertEqual('You do not have krastavica', res)

    def test_feed_with_less_food(self):

        self.s.food = {'domat': 50.50}
        self.s.pets = ['reksi']
        res = self.s.feed_pet('domat', 'reksi')
        self.assertEqual('Adding food...', res)
        self.assertEqual({'domat': 1050.50}, self.s.food)

    def test_successful_feed(self):

        self.s.food = {'domat': 101.50}
        self.s.pets = ['reksi']
        res = self.s.feed_pet('domat', 'reksi')
        self.assertEqual("reksi was successfully fed", res)
        self.assertEqual({'domat': 1.50}, self.s.food)

    def test_repr(self):

        actual_result = self.s.__repr__()
        expected_result = f'Shop {self.s.name}:\n' \
                          f'Pets: {", ".join(self.s.pets)}'
        self.assertEqual(expected_result, actual_result)

if __name__ == "__main__":
    unittest.main()
