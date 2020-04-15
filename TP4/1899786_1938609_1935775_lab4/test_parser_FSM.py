from collections import Counter
from functools import total_ordering
from Parser_FSM import ApplyRules
import unittest


class TestParser(unittest.TestCase):

    # t1
    def test_PREFIX_loop(self):
        str = "a = 1"
        parse = ApplyRules(str)
        parse.run()
        self.assertEqual(parse.current_state, "STATE: PREFIX")

    # t2
    def test_SUBJECT_loop(self):
        str = "a = (132"
        parse = ApplyRules(str)
        parse.run()
        self.assertEqual(parse.current_state, "STATE: SUBJECT")

    # t3
    def test_arrival_to_NEW_GROUP(self):
        str = "a = (132) & ("
        parse = ApplyRules(str)
        parse.run()
        self.assertEqual(parse.current_state, "STATE: NEW_GROUP")

    # t4
    def test_arrival_to_PREFIX_after_OPERATOR(self):
        str = "a = (132) & z"
        parse = ApplyRules(str)
        parse.run()
        self.assertEqual(parse.current_state, "STATE: PREFIX")

    # t5
    def test_arrival_to_OPERATOR_after_END_GROUP(self):
        str = "a = ( (132) )&"
        parse = ApplyRules(str)
        parse.run()
        self.assertEqual(parse.current_state, "STATE: OPERATOR")

    # t6
    def test_arrival_to_END_GROUP_after_END_RULE(self):
        str = "a = ( (132) ) "
        parse = ApplyRules(str)
        parse.run()
        self.assertEqual(parse.current_state, "STATE: END_GROUP")


if __name__ == '__main__':
    unittest.main()
