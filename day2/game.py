class Game:
    def __init__(self, game:dict[str, list[dict[str, int]]|str]):
        self.__game = game

    @property
    def game_id(self) -> int:
        return self.__game["game"]

    @property
    def power(self) -> int:
        return self.max_color("red") * self.max_color("green") * self.max_color("blue")
    
    def max_color(self, color: str):
        max = 0
        for subset in self.__game["subsets"]:
            if color in subset.keys() and subset[color] > max:
                max = subset[color]
        return max
    
    def is_valid_game(self, **kwargs) -> bool:
        for color in kwargs.keys():
            if not self.is_valid_color(color, kwargs[color]):
                return False
        return True
    
    def is_valid_color(self, color: str, count: int) -> bool:
        for subset in self.__game["subsets"]:
            if color in subset.keys():
                if subset[color] > count:
                    return False
        return True