import unittest
from markov import plotitsyn_markov as markov


class TestMarkovAlgorithm(unittest.TestCase):
    def test_correct_markov(self):
        result = markov.markov("abc", "ab-a aa-c", "abab")
        self.assertEqual(result, "c")

    def test_infinite_loop(self):
        result = markov.markov("abc", "a-sa aa-c", "abab")
        self.assertEqual(result, "Rule: a - sa is bad. Infinite Loop")

    def test_not_alphabet_word(self):
        result = markov.markov("abc", "ab-a aa-c", "asbab")
        self.assertEqual(result, "Word have symbols which are not in alphabet")
