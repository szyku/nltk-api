import unittest;

import collections

from nltk_api.definition.processor import DefinitionProcessor
from nltk_api.definition.processed_word import ProcessedWord


class DefinitionProcessorTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._processor = DefinitionProcessor()

    @classmethod
    def tearDownClass(cls):
        del cls._processor

    def testLookUpDefinitions(self):
        processor = self._processor
        actual_result = processor.look_up("cat")

        self.assertIsInstance(actual_result, collections.Sequence)
        self.assertIsInstance(actual_result[0], dict)

        entry = actual_result[0]

        self.assertIsNotNone(entry.get('definition', None))
        self.assertIsNotNone(entry.get('word', None))

        definition = entry.get('definition')
        word = entry.get('word')

        self.assertIsInstance(definition, str)
        self.assertIsInstance(word, ProcessedWord)

    def testIfOnlyCertainPartOfSpeechIsReturnedOnRequest(self):
        processor = self._processor
        result_set = processor.look_up('cat', 'verb')

        for entry in result_set:
            word = entry.get('word')
            definition = entry.get('definition')
            self.assertTrue(word.is_part_of_speech('verb'))
            self.assertIsNotNone(word.word())
            self.assertIsNotNone(definition)
            self.assertGreater(len(definition), 0)

    def testIfWordsAreFilteredOut(self):
        processor = self._processor
        result_set = processor.look_up('cat', similar=False)

        for entry in result_set:
            word = entry.get('word')
            self.assertTrue(word.word() == 'cat')

        filtered_count = len(result_set)

        similar_result_set = processor.look_up('cat', similar=True)
        self.assertGreater(len(similar_result_set), filtered_count)

    def testChecksIfDataEnteredIsCorrect(self):
        processor = self._processor
        self.assertRaises(ValueError, processor.look_up, 'dddd', 'i don\'t exist')
