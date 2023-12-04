import unittest
from day2.main import parse_line

test_cases = [
    ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green', {
        "game": 1, "subsets": [{"blue": 3, "red": 4}, {"red": 1, "green": 2, "blue": 6}, {"green": 2}]
    }],
    ['Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue', {
        "game": 2, "subsets": [{"blue": 1, "green": 2}, {"green": 3, "blue": 4, "red": 1}, {"green": 1, "blue": 1}]
    }]
]

class TestParsing(unittest.TestCase):

    def test_should_parse_correctly(self):
        for test_case in test_cases:
            self.assertDictEqual(parse_line(test_case[0]), test_case[1])
