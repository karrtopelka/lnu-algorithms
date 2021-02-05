import unittest
from postfix import postfix
from postfix_eval import postfix_evaluation


class MyTestCase(unittest.TestCase):
    def test_simple_int(self):
        self.assertEqual(postfix_evaluation(postfix("5 + 5")), 10.00)

    def test_medium_int(self):
        self.assertEqual(postfix_evaluation(postfix("( 5 + 5 * 3 ) / 12 + ( 2 / 1 )")), 3.67)


if __name__ == '__main__':
    unittest.main()
