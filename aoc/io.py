def read_lines(filepath: str) -> list[str]:
    return [line.replace("\n", "") for line in open(filepath)]