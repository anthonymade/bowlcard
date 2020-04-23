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
            self.line.score_frame(frame1_bowl1, frame1_bowl2)
            self.line.score_frame(frame2_bowl1, frame2_bowl2)

        with then:
            self.line.get_score() == expected_score

        with where:
            frame1_bowl1 = [6]
            frame1_bowl2 = [4]
            frame2_bowl1 = [3]
            frame2_bowl2 = [2]
            expected_score = [10 + 3 + 3 + 2]

    def a_frame_score_is_not_added_to_the_total_until_its_value_is_known(self):

        with when:
            self.line.score_frame(4, 6)

        with then:
            self.line.get_score() == 0


    def we_can_score_a_strike(self):

        with when:
            self.line.score_frame(10, 0)

        with then:
            self.line.get_score() == 0


    def the_frame_score_for_a_strike_includes_the_next_two_bowls(self):

        with when:
            self.line.score_frame(10, 0) # 17
            self.line.score_frame(2, 5)  # 7

        with then:
            self.line.get_score() == 24


    def two_consecutive_strikes_will_have_no_score(self):

        with when:
            self.line.score_frame(10, 0) # ?
            self.line.score_frame(10, 0) # ?

        with then:
            self.line.get_score() == 0


    def can_score_two_consecutive_strikes_when_next_frame_scores(self):

        with when:
            self.line.score_frame(10, 0) # 23
            self.line.score_frame(10, 0) # 14
            self.line.score_frame(3, 1) # 4

        with then:
            self.line.get_score() == 41


    def bowl1_cannot_be_greater_than_10(self):

        with when:
            self.line.score_frame(11, 0)

        with then:
            e = thrown(Exception)
            str(e[1]) == 'bowl 1 cannot be graeter than 10, it was 11'