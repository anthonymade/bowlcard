from nimoy.specification import Specification
from bowlcard.line import Line


class LineSpec(Specification):

    def a_new_line_will_return_a_score_of_zero(self):

        with expect:
            Line().get_score() == 0

