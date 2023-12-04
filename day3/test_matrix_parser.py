import unittest
from day3.matrix_parser import MatrixParser
from day3.part_number import PartNumber

test_cases_symbols = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#..."
]

test_cases_numbers = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]

class TestMatrixParser(unittest.TestCase):

    def test_should_add_adjacency(self):
        mp = MatrixParser(test_cases_symbols)
        mp.add_adjacency(4, 4)
        self.assertSetEqual(mp.adjacency_coordinates, {"4_4", "3_4", "5_4", "4_3", "4_5", "3_3", "5_5", "3_5", "5_3", "5_4"})

    def test_should_validate_part_number_adjacency(self):
        mp = MatrixParser(test_cases_symbols)
        mp.parse_symbols()
        self.assertTrue(mp.part_number_in_adjacency(PartNumber("467", 0, 0, 2)))
        self.assertFalse(mp.part_number_in_adjacency(PartNumber("114", 0, 5, 7)))

    def test_should_parse_symbols(self):
        mp = MatrixParser(test_cases_symbols)
        mp.parse_symbols()
        self.assertEqual(len(mp.adjacency_coordinates), 18)
        self.assertSetEqual(mp.star_coordinates, {"1_3"})

    def test_should_parse_part_numbers(self):
        mp = MatrixParser([])
        part_numbers = mp.parse_part_number_line("467..114..", 5)
        self.assertEqual(len(part_numbers), 2)
        self.assertEqual(part_numbers[0].value, 467)
        self.assertEqual(part_numbers[1].value, 114)
        self.assertSetEqual(part_numbers[0].coordinates, {"5_0", "5_1", "5_2"})
        self.assertSetEqual(part_numbers[1].coordinates, {"5_5", "5_6", "5_7"})

    def test_should_generate_sum_valid_part_numbers(self):
        mp = MatrixParser(test_cases_numbers)
        mp.parse_symbols()
        mp.parse_valid_part_numbers()
        self.assertEqual(mp.valid_part_number_sum, 4361)

    def test_should_get_adjacency_coordinates(self):
        mp = MatrixParser([])
        self.assertSetEqual(mp.get_adjacency_coordinates("4_4"), {"4_4", "3_4", "5_4", "4_3", "4_5", "3_3", "5_5", "3_5", "5_3", "5_4"})

    def test_should_get_adjacent_part_numbers(self):
        mp = MatrixParser(test_cases_numbers)
        mp.parse_symbols()
        mp.parse_valid_part_numbers()
        pms = mp.get_adjacent_part_numbers("1_3")
        self.assertEqual(len(pms), 2)
        pms = mp.get_adjacent_part_numbers("4_3")
        self.assertEqual(len(pms), 1)
        pms = mp.get_adjacent_part_numbers("8_5")
        self.assertEqual(len(pms), 2)

    def test_should_get_gear_sum(self):
        mp = MatrixParser(test_cases_numbers)
        mp.parse_symbols()
        mp.parse_valid_part_numbers()
        mp.parse_gears()
        self.assertEqual(mp.gear_sum, 467835)
