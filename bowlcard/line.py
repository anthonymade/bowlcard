class Line:

    def __init__(self):
        self.__frames = []

    def get_score(self) -> int:
        score = 0
        for frame in self.__frames:
            score += frame.bowl1
            score += frame.bowl2
        return score

    def score_frame(self, bowl1: int, bowl2: int) -> None:
        self.__frames.append(Frame(bowl1, bowl2))

    def score_spare(self, bowl1: int) -> None:
        pass

    def get_frame(self, frame_number: int):
        return self.__frames[frame_number -1]

class Frame:

    bowl1 = 0
    bowl2 = 0

    def __init__(self, bowl1: int, bowl2: int):
        self.bowl1 = bowl1
        self.bowl2 = bowl2
