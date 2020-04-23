from nimoy.specification import Specification
from bowlcard.line import Line


class LineSpec(Specification):

    def a_new_line_will_return_a_score_of_zero(self):

        with expect:
            Line().get_score() == 0


    def we_can_score_a_frame(self):

        with given:
            line = Line()

        with when:
            line.score_frame(bowl1, bowl2)

        with then:
            line.get_score() == expected_score

        with where:
            bowl1 = [3]
            bowl2 = [4]
            expected_score = [7]


    def we_can_get_the_individual_scores_for_a_frame(self):

        with given:
            line = Line()

        with when:
            line.score_frame(bowl1, bowl2)

        with then:
            frame_score = line.get_frame(1)
            frame_score.bowl1 == bowl1
            frame_score.bowl2 == bowl2

        with where:
            bowl1 = [2]
            bowl2 = [1]


    def we_can_score_multiple_frames(self):

        with given:
            line = Line()

        with when:
            line.score_frame(frame1_bowl1, frame1_bowl2)
            line.score_frame(frame2_bowl1, frame2_bowl2)

        with then:
            line.get_score() == expected_score
            line.get_frame(1).bowl1 == frame1_bowl1
            line.get_frame(1).bowl2 == frame1_bowl2
            line.get_frame(2).bowl1 == frame2_bowl1
            line.get_frame(2).bowl2 == frame2_bowl2

        with where:
            frame1_bowl1 | frame1_bowl2 | frame2_bowl1 | frame2_bowl2 | expected_score
            3            | 2            | 4            | 1            | 10
            5            | 2            | 3            | 4            | 14
