class Line:

    def __init__(self):
        self.__frames = []

    def get_score(self) -> int:
        score = 0
        last_index = len(self.__frames) - 1
        for i in range(len(self.__frames)):
            frame_score = self.__frames[i].bowl1 + self.__frames[i].bowl2
            if frame_score == 10:
                if i < last_index:
                    score += frame_score
                    score += self.__frames[i + 1].bowl1
            else:
                score += frame_score
        return score

    def score_frame(self, bowl1: int, bowl2: int) -> None:
        self.__frames.append(Frame(bowl1, bowl2))

    def score_spare(self, bowl1: int) -> None:
        self.__frames.append(Frame(bowl1, 10 - bowl1))

    def get_frame(self, frame_number: int):
        return self.__frames[frame_number -1]

class Frame:

    bowl1 = 0
    bowl2 = 0

    def __init__(self, bowl1: int, bowl2: int):
        self.bowl1 = bowl1
        self.bowl2 = bowl2
