import unittest
from day2.main import parse_line
from day2.game import Game

test_cases_valid_games = [
    ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green', True],
    ['Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue', True],
    ['Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red', False],
    ['Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red', False]
]

test_cases_power = [
    ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green', 48],
    ['Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue', 12],
    ['Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red', 1560],
    ['Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red', 630],
    ['Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green', 36],
    ['Game 100: 4 red, 2 blue, 4 green; 2 green, 1 red, 1 blue; 3 green, 4 blue, 5 red; 18 red, 2 blue; 9 red, 5 green, 4 blue', 18 * 5 * 4]
]

class TestGame(unittest.TestCase):

    def test_should_filter_invalid_games(self):
        for test_case in test_cases_valid_games:
            game = Game(parse_line(test_case[0]))
            self.assertEqual(game.is_valid_game(red=12, green=13, blue=14), test_case[1], test_case[0])

    def test_color_max_value_of_game(self):
        game = Game(parse_line(test_cases_power[0][0]))
        self.assertEqual(game.max_color("red"), 4)
        self.assertEqual(game.max_color("green"), 2)
        self.assertEqual(game.max_color("blue"), 6)

    def test_should_calculate_power_of_games(self):
        for test_case in test_cases_power:
            game = Game(parse_line(test_case[0]))
            self.assertEqual(game.power, test_case[1], test_case[0])
