import re
from day3.part_number import PartNumber

part_numbers_regex = re.compile("\d+")

class MatrixParser:
    def __init__(self, lines: list[str] = []):
        self.__lines = lines
        self.__adjacency_coordinates = set()
        self.__star_coordinates = set()
        self.__valid_part_numbers = []
        self.__gear_part_numbers = []

    @property
    def star_coordinates(self) -> set:
        return self.__star_coordinates

    @property
    def adjacency_coordinates(self) -> set:
        return self.__adjacency_coordinates.copy()
    
    @property
    def gear_sum(self) -> int:
        return sum([part_number for part_number in self.__gear_part_numbers]) 
    
    @property
    def valid_part_number_sum(self) -> int:
        return sum([part_number.value for part_number in self.__valid_part_numbers])
    
    def part_number_in_adjacency(self, part_number: PartNumber) -> bool:
        for coordinate in part_number.coordinates:
            if coordinate in self.__adjacency_coordinates:
                return True
        return False
    
    def parse_gears(self):
        for star_coordinate in self.__star_coordinates:
            pms = self.get_adjacent_part_numbers(star_coordinate)
            if len(pms) > 1:
                product = 1
                for pm in pms:
                    product = product * pm.value
                self.__gear_part_numbers.append(product)
        
    def parse_valid_part_numbers(self):
        for row, line in enumerate(self.__lines):
            part_numbers = self.parse_part_number_line(line, row)
            for part_number in part_numbers:
                if self.part_number_in_adjacency(part_number):
                    self.__valid_part_numbers.append(part_number)
            
    def parse_part_number_line(self, line, row) -> list[PartNumber]:
        part_numbers = []
        for match in part_numbers_regex.finditer(line):
            part_numbers.append(PartNumber(match.group(0), row, match.start(0), match.end(0)-1))
        return part_numbers

    def parse_symbols(self):
        for row, line in enumerate(self.__lines):
            for col, character in enumerate(line):
                if character not in ".0123456789":
                    self.add_adjacency(row, col)
                if character == "*":
                    self.__star_coordinates.add("{}_{}".format(row, col))

    def get_adjacent_part_numbers(self, coordinate: str) -> list[PartNumber]:
        adjacent_part_numbers = []
        adjacency_coordinates = self.get_adjacency_coordinates(coordinate)
        for part_number in self.__valid_part_numbers:
            if len(adjacency_coordinates.intersection(part_number.coordinates)) > 0:
                adjacent_part_numbers.append(part_number)
        return adjacent_part_numbers

    def get_adjacency_coordinates(self, coordinate: str) -> set[str]:
        coordinates = set()
        coordinate_parts = coordinate.split("_")
        row = int(coordinate_parts[0])
        col = int(coordinate_parts[1])
        for r in (-1, 0, 1):
            for c in (-1, 0, 1):
                coordinates.add("{}_{}".format(row - r, col - c))
        return coordinates

    def add_adjacency(self, row: int, col: int):
        for r in (-1, 0, 1):
            for c in (-1, 0, 1):
                self.__adjacency_coordinates.add("{}_{}".format(row - r, col - c))
