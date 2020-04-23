from nimoy.specification import Specification
from bowlcard.line import Line


class LineSpec(Specification):

    def setUp(self) -> None:
        self.line = Line()

    def a_new_line_will_return_a_score_of_zero(self):

        with expect:
            self.line.get_score() == 0


    def we_can_score_multiple_frames(self):

        with given:
            self.line = Line()

        with when:
            self.line.score_frame(frame1_bowl1, frame1_bowl2)
            self.line.score_frame(frame2_bowl1, frame2_bowl2)

        with then:
            self.line.get_score() == expected_score
            self.line.get_frame(1).bowl1 == frame1_bowl1
            self.line.get_frame(1).bowl2 == frame1_bowl2
            self.line.get_frame(2).bowl1 == frame2_bowl1
            self.line.get_frame(2).bowl2 == frame2_bowl2

        with where:
            frame1_bowl1 | frame1_bowl2 | frame2_bowl1 | frame2_bowl2 | expected_score
            3            | 2            | 4            | 1            | 10
            5            | 2            | 3            | 4            | 14


    def we_can_score_a_spare(self):

        with when:
            self.line.score_spare(bowl1)
            self.line.score_frame(frame2_bowl1, frame2_bowl2)

        with then:
            self.line.get_score() == expected_score

        with where:
            bowl1 = [6]
            frame2_bowl1 = [3]
            frame2_bowl2 = [2]
            expected_score = [10 + 3 + 3 + 2]