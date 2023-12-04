class PartNumber:
    def __init__(self, value, row, start_col, end_col):
        self.__value = value
        self.__row = row
        self.__start = start_col
        self.__end = end_col

    @property
    def coordinates(self) -> set[str]:
        return {"{}_{}".format(self.__row, index) for index in range(self.__start, self.__end + 1)}
    
    @property
    def value(self) -> int:
        return int(self.__value)
    
    
