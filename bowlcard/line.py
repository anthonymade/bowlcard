class Line:

    def __init__(self):
        self.__score = 0

    def get_score(self) -> int:
        return self.__score

    def score_frame(self, bowl1: int, bowl2: int):
        self.__score = self.__score + bowl1 + bowl2