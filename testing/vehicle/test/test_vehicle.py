from python_testing.vehicle.project.vehicle import Vehicle
import unittest

class VehicleTests(unittest.TestCase):

    def setUp(self):

        self.vehicle = Vehicle(50.5, 231.5)

    def test_vehicle_is_initialised_correctly(self):

        self.assertEqual(50.5, self.vehicle.fuel)
        self.assertEqual(231.5, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_refuel_above_capacity_raises(self):

        self.assertEqual(50.5, self.vehicle.fuel)
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_adds_fuel(self):

        self.vehicle.drive(15)
        self.vehicle.refuel(10)
        self.assertEqual(41.75, self.vehicle.fuel)

    def test_drive(self):

        self.assertEqual(50.5, self.vehicle.fuel)
        self.vehicle.drive(15)
        self.assertEqual(31.75, self.vehicle.fuel)

    def test_drive_not_enough_fuel_raises(self):

        self.assertEqual(50.5, self.vehicle.fuel)
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_with_zero_fuel_raises(self):

        self.assertEqual(50.5, self.vehicle.fuel)
        self.vehicle.drive(40.4)
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(2)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_print(self):

        actual_result = self.vehicle.__str__()
        expected_result = f"The vehicle has 231.5 " \
                        f"horse power with {self.vehicle.fuel} fuel left and 1.25 fuel consumption"
        self.assertEqual(expected_result, actual_result)

if __name__ == "__main__":
    unittest.main()