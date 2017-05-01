import unittest

from nltk_api.lemma.processor import LemmaProcessor


class LemmaProcessorTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._processor = LemmaProcessor()

    @classmethod
    def tearDownClass(cls):
        del cls._processor

    def testProducesLemma(self):
        actual = self._processor.lemma('jogging', 'verb')
        expected = {'lemma': 'jog', 'partOfSpeech': 'verb'}

        self.assertDictEqual(actual, expected)

        actual_from_all = self._processor.all_lemma('jogging')
        has_set = False
        for element in actual_from_all:
            if element == expected:
                has_set = True
                break

        self.assertTrue(has_set, 'The result set does not contain a correct lemma for jogging.')
