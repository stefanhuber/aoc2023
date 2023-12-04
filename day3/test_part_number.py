import unittest
from day3.part_number import PartNumber

class TestPartNumber(unittest.TestCase):
    def test_should_return_correct_coordinates(self):
        pm = PartNumber("123", 4, 3, 5)
        self.assertSetEqual(pm.coordinates, {"4_3", "4_4", "4_5"})
