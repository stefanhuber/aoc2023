import re
from aoc.io import read_lines

number_regex = re.compile("\d+")

#Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
def parse_line(line:str) -> dict:
    split1 = line.split(":")
    split2 = split1[1].split("|")

    return {
        "winning_numbers": set(number_regex.findall(split2[0])),
        "collected_numbers": set(number_regex.findall(split2[1]))
    }

def calculate_matches(numbers: dict[str, set[str]]) -> int:
    return len(numbers["winning_numbers"].intersection(numbers["collected_numbers"]))

def calculate_points(numbers: dict[str, set[str]]) -> int:
    return int(pow(2, (calculate_matches(numbers) - 1)))

def main():
    print("DAY 4")
    day4_1()
    day4_2()

def day4_1():
    lines = read_lines("./day4/day4.txt")
    points = sum([calculate_points(parse_line(line)) for line in lines])
    print(" 1: {}".format(points))

def day4_2():
    lines = read_lines("./day4/day4.txt")
    copies = {i: 1 for i in range(1, len(lines) + 1)}

    for index, line in enumerate(lines):
        card_number = index + 1
        matches = calculate_matches(parse_line(line))
        mutltiplier = copies[card_number]
        proposed_max_card_number = card_number + matches + 1
        max_card_number = proposed_max_card_number if proposed_max_card_number <= len(lines) + 1 else len(lines) + 1
        for i in range(card_number + 1, max_card_number):
            copies[i] = copies[i] + mutltiplier
    result = 0
    for card, count in copies.items():
        result += count
    print(" 2: {}".format(result))

