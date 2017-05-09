import unittest

from nltk_api.tag.sentence import tag_sentences


class SentenceTaggerTestCase(unittest.TestCase):
    def testTagWithSymbols(self):
        test_sentences = ['I walk over him', 'I like to watch']
        actual = tag_sentences(test_sentences, True)
        self.assertTupleEqual(('I', 'PRP'), actual[0][0])
        self.assertTupleEqual(('walk', 'VBP'), actual[0][1])

    def testTagWithHumanizedSymbols(self):
        test_sentences = ['I walk over him', 'I like to watch']
        actual = tag_sentences(test_sentences, False)
        self.assertTupleEqual(('I', 'pronoun_personal'), actual[0][0])
        self.assertTupleEqual(('walk', 'verb_present_not_3rd_person'), actual[0][1])
