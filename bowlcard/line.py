class Line:

    def __init__(self):
        self.__score = 0
        self.__frames = []

    def get_score(self) -> int:
        return self.__score

    def score_frame(self, bowl1: int, bowl2: int):
        self.__score = self.__score + bowl1 + bowl2
        self.__frames.append(Frame(bowl1, bowl2))

    def get_frame(self, frame_number: int):
        return self.__frames[frame_number -1]

class Frame:

    bowl1 = 0
    bowl2 = 0

    def __init__(self, bowl1: int, bowl2: int):
        self.bowl1 = bowl1
        self.bowl2 = bowl2
