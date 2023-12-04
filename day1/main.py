import re
from aoc.io import read_lines


number_regex = [
    re.compile("[0-9]{1}"),
    re.compile("(?=([0-9]{1}|one|two|three|four|five|six|seven|eight|nine))")
]


def main():
    lines = read_lines("./day1/day1.txt")
    print("DAY 1")
    print(" 1: {}".format(sum([extract_number(line, 0) for line in lines])))
    print(" 2: {}".format(sum([extract_number(line, 1) for line in lines])))
   

def extract_number(line:str, regex_index=1) -> int:
    all_numbers = number_regex[regex_index].findall(line)
    return int("{}{}".format(as_number(all_numbers[:1][0]), as_number(all_numbers[-1:][0])))


def as_number(text) -> str:
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    return text if len(text) == 1 else str(1 + numbers.index(text))
