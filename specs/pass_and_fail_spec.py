from nimoy.specification import Specification

class TestTestsSpec(Specification):

    def passing_feature(self):

        with expect:
            True == True

    def failing_feature(self):

        with expect:
            True == False

