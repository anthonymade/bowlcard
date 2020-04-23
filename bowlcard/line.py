class Line:

    def __init__(self):
        self.__frames = []

    def get_score(self) -> int:
        score = 0
        last_index = len(self.__frames) - 1
        for i in range(min(len(self.__frames), 10)):
            frame_score = self.__frames[i].bowl1 + self.__frames[i].bowl2
            if self.__frames[i].bowl1 == 10:
                if i < last_index and (self.__frames[i + 1].bowl1 != 10 or i == 9):
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
        if bowl1 + bowl2 > 10 and len(self.__frames) != 10:
            raise Exception(f"you cannot score more than 10 with your two bowls, total was {bowl1 + bowl2}")
        if self.is_game_over():
            raise Exception('the game is over, you cannot score')
        if len(self.__frames) == 10 and self.__frames[9].bowl1 != 10 and bowl2 != 0:
            raise Exception(f"you only have 1 extra bowl after a 10th frame spare, bowl 2 must be zero but was {bowl2}")
        self.__frames.append(Frame(bowl1, bowl2))

    def __validate_bowl_value(self, bowl_number: int, bowl_value: int) -> None:
        if bowl_value > 10:
            raise Exception(f"bowl {bowl_number} cannot be greater than 10, it was {bowl_value}")
        if bowl_value < 0:
            raise Exception(f"bowl {bowl_number} cannot be less than 0, it was {bowl_value}")

    def get_frame(self, frame_number: int):
        return self.__frames[frame_number -1]

    def is_game_over(self) -> bool:
        if len(self.__frames) == 10:
            return self.__frames[9].bowl1 + self.__frames[9].bowl2 != 10
        return len(self.__frames) > 9

class Frame:

    bowl1 = 0
    bowl2 = 0

    def __init__(self, bowl1: int, bowl2: int):
        self.bowl1 = bowl1
        self.bowl2 = bowl2
