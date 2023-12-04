import unittest
from day4.main import parse_line, calculate_points

class TestParsingLine(unittest.TestCase):

    def test_should_parse_line(self):
        numbers = parse_line("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1")
        self.assertSetEqual(numbers["winning_numbers"], {'1', '21', '53', '59', '44'})
        self.assertSetEqual(numbers["collected_numbers"], {'69', '82', '63', '72', '16', '21', '14', '1'})

    def test_should_calculate_points(self):
        points = calculate_points({
            "winning_numbers": {'1', '21', '53', '59', '44'},
            "collected_numbers": {'69', '82', '63', '72', '16', '21', '14', '1'}
        })
        self.assertEqual(points, 2)