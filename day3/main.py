from aoc.io import read_lines
from day3.matrix_parser import MatrixParser

def main():
    print("DAY 3")
    day3_1()
    day3_2()


def day3_1():
    mp = MatrixParser(read_lines("./day3/day3.txt"))
    mp.parse_symbols()
    mp.parse_valid_part_numbers()
    print(" 1: {}".format(mp.valid_part_number_sum))


def day3_2():
    mp = MatrixParser(read_lines("./day3/day3.txt"))
    mp.parse_symbols()
    mp.parse_valid_part_numbers()
    mp.parse_gears()
    print(" 2: {}".format(mp.gear_sum))