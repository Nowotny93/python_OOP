from python_oop_exams.project_16AUG2020 import Train

import unittest

class TrainTests(unittest.TestCase):

    def setUp(self):

        self.s = Train('Harry', 2)

    def test_init(self):

        self.assertEqual('Harry', self.s.name)
        self.assertEqual(2, self.s.capacity)
        self.assertEqual([], self.s.passengers)

    def test_add_passenger(self):

        self.s.passengers = ['gosho', 'kiko']
        with self.assertRaises(ValueError) as ex:
            self.s.add('pesho')
        self.assertEqual("Train is full", str(ex.exception))

    def test_add_existing_passenger(self):

        self.s.passengers = ['gosho']
        with self.assertRaises(ValueError) as ex:
            self.s.add('gosho')
        self.assertEqual("Passenger gosho Exists", str(ex.exception))

    def test_add_new_passenger_with_free_capa(self):

        self.s.passengers = ['gosho']
        res = self.s.add('meto')
        self.assertEqual('Added passenger meto', res)
        self.assertEqual(['gosho', 'meto'], self.s.passengers)

    def test_remove_non_existing_passenger(self):

        self.s.passengers = ['gosho', 'kiko']
        with self.assertRaises(ValueError) as ex:
            self.s.remove('meto')
        self.assertEqual('Passenger Not Found', str(ex.exception))

    def test_remove_existing_passenger(self):

        self.s.passengers = ['gosho', 'kiko']
        res = self.s.remove('gosho')
        self.assertEqual('Removed gosho', res)
        self.assertEqual(['kiko'], self.s.passengers)


if __name__ == "__main__":
    unittest.main()