class Line:

    def __init__(self):
        self.__frames = []

    def get_score(self) -> int:
        score = 0
        last_index = len(self.__frames) - 1
        for i in range(len(self.__frames)):
            frame_score = self.__frames[i].bowl1 + self.__frames[i].bowl2
            if self.__frames[i].bowl1 == 10:
                if i < last_index and self.__frames[i + 1].bowl1 != 10:
                    score += frame_score
                    score += self.__frames[i + 1].bowl1
                    score += self.__frames[i + 1].bowl2
                if i < last_index -1:
                    score += frame_score
                    score += self.__frames[i + 1].bowl1
                    score += self.__frames[i + 2].bowl1
            elif frame_score == 10:
                if i < last_index:
                    score += frame_score
                    score += self.__frames[i + 1].bowl1
            else:
                score += frame_score
        return score

    def score_frame(self, bowl1: int, bowl2: int) -> None:
        self.__validate_bowl_value(1, bowl1)
        self.__validate_bowl_value(2, bowl2)
        if bowl1 < 0:
            raise Exception(f"bowl 1 cannot be less than 0, it was {bowl1}")
        self.__frames.append(Frame(bowl1, bowl2))

    def __validate_bowl_value(self, bowl_number: int, bowl_value: int) -> None:
        if bowl_value > 10:
            raise Exception(f"bowl {bowl_number} cannot be greater than 10, it was {bowl_value}")

    def get_frame(self, frame_number: int):
        return self.__frames[frame_number -1]

class Frame:

    bowl1 = 0
    bowl2 = 0

    def __init__(self, bowl1: int, bowl2: int):
        self.bowl1 = bowl1
        self.bowl2 = bowl2
