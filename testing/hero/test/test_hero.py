from python_testing.hero.project.hero import Hero

import unittest

class HeroTests(unittest.TestCase):

    def setUp(self):

        self.hero = Hero('Test', 8, 50, 10)
        self.enemy = Hero('Test1', 8, 50, 10)
        self.strong_hero = Hero('Test2', 1000, 200000, 3000)

    def test_hero_is_initialised_correctly(self):

        #Assert
        self.assertEqual("Test", self.hero.username)
        self.assertEqual(8, self.hero.level)
        self.assertEqual(50, self.hero.health)
        self.assertEqual(10, self.hero.damage)

    def test_check_username_raises(self):

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_health_less_than_zero(self):

        self.hero.health = -2
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_health_is_zero(self):

        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_enemy_health_less_than_zero(self):

        self.enemy.health = -2
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ex.exception))

    def test_enemy_health_is_zero(self):

        self.enemy.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ex.exception))

    def test_battle_draw(self):

        res = self.hero.battle(self.enemy)
        self.assertEqual("Draw", res)

    def test_win(self):

        res = self.strong_hero.battle(self.enemy)
        self.assertEqual("You win", res)
        self.assertEqual(199925, self.strong_hero.health)
        self.assertEqual(3005, self.strong_hero.damage)
        self.assertEqual(1001, self.strong_hero.level)
        self.assertEqual(-2999950, self.enemy.health)
        self.assertEqual(10, self.enemy.damage)
        self.assertEqual(8, self.enemy.level)

    def test_lose(self):

        res = self.hero.battle(self.strong_hero)
        self.assertEqual("You lose", res)
        self.assertEqual(199925, self.strong_hero.health)
        self.assertEqual(3005, self.strong_hero.damage)
        self.assertEqual(1001, self.strong_hero.level)
        self.assertEqual(-2999950, self.hero.health)
        self.assertEqual(10, self.hero.damage)
        self.assertEqual(8, self.hero.level)

    def test_str(self):
        actual_result = self.hero.__str__()
        expected_result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
                            f"Health: {self.hero.health}\n" \
                            f"Damage: {self.hero.damage}\n"
        self.assertEqual(expected_result, actual_result)

if __name__ == "__main__":
    unittest.main()