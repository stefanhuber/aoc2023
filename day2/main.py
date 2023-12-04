import re
from aoc.io import read_lines
from day2.game import Game


cube_regex = re.compile(" (\d+) (blue|green|red)")


def main():
    print("DAY 2")
    example1()
    day2_1()
    example2()
    day2_2()

def example1():
    result = 0
    lines = read_lines("./day2/example1.txt")
    for line in lines:
        game = Game(parse_line(line))
        if game.is_valid_game(red=12, green=13, blue=14):
            result += game.game_id
    print(" example 1: {}".format(result))


def day2_1():
    result = 0
    lines = read_lines("./day2/day2.txt")
    for line in lines:
        game = Game(parse_line(line))
        if game.is_valid_game(red=12, green=13, blue=14):
            result += game.game_id
    print(" 1: {}".format(result))


def example2():
    result = 0
    lines = read_lines("./day2/example1.txt")
    for line in lines:
        result += Game(parse_line(line)).power
    print(" example 2: {}".format(result))


def day2_2():
    result = 0
    lines = read_lines("./day2/day2.txt")
    for line in lines:
        result += Game(parse_line(line)).power
    print(" 2: {}".format(result))


def parse_line(line: str) -> dict:
    game_index = line.find(":")

    result = {
        "game": int(line[:game_index].split(" ")[1]),
        "subsets": []
    }

    subsets = line[game_index+1:].split(";")
    for subset in subsets:
        parsed_subset = dict()
        cubes = subset.split(",")
        for cube in cubes:
            cube_match = cube_regex.match(cube)
            parsed_subset[cube_match.group(2)] = int(cube_match.group(1))
        result["subsets"].append(parsed_subset)

    return result