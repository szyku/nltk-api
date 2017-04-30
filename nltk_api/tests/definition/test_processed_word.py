import unittest;

from nltk.corpus.reader.wordnet import NOUN, ADV, ADJ, ADJ_SAT, VERB

from nltk_api.definition.processed_word import ProcessedWord


class ProcessedWordTestCase(unittest.TestCase):
    def testSysnetWordDissect(self):
        test_string = 'cat.n.1'
        test_subject = ProcessedWord(test_string)

        self.failUnless(test_subject.raw_word() == "cat")
        self.failUnless(test_subject.raw_part_of_speech() == NOUN)
        self.failUnless(test_subject.word_index() == 1)

        self.assertEqual(test_subject.word(), 'cat')
        self.failUnless(test_subject.part_of_speech() == "noun")
        self.failUnless(test_subject.word_index() == 1)

    def testDetectsAllPartsOfSpeech(self):
        test_noun = ProcessedWord('noun.'+NOUN+'.1')
        test_adverb = ProcessedWord('adverb.' + ADV + '.1')
        test_adjective = ProcessedWord('adjective.' + ADJ + '.1')
        test_adjective_satellite = ProcessedWord('adjective.' + ADJ_SAT + '.1')
        test_verb = ProcessedWord('verb.' + VERB + '.1')

        self.assertEqual('noun', test_noun.part_of_speech())
        self.assertEqual('adverb', test_adverb.part_of_speech())
        self.assertEqual('adjective', test_adjective.part_of_speech())
        self.assertEqual('adjective', test_adjective_satellite.part_of_speech())
        self.assertEqual('verb', test_verb.part_of_speech())

    def testHumanizesDashedAndAccentedWords(self):
        test_complex = ProcessedWord('turnip_jack-o\'-lantern.'+NOUN+'.1')

        self.assertEqual('turnip jack-o\'-lantern', test_complex.word())

    def testWrongDataReaction(self):
        self.assertRaises(TypeError, ProcessedWord, 123)
        self.assertRaises(ValueError, ProcessedWord, 'not.complete')

        test_obj = ProcessedWord('noun.n.1')
        self.assertRaises(TypeError, test_obj.is_part_of_speech('q'))
