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