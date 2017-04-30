from nltk.corpus import wordnet
from nltk_api.definition.processed_word import ProcessedWord
from nltk_api.lemma.processor import POS


class DefinitionProcessor(object):
    def __init__(self):
        pass

    def look_up(self, word, pos=None, similar=True):
        if pos not in POS and pos is not None:
            raise ValueError('Passed pos is not recognized.')

        synsets = wordnet.synsets(word, POS.get(pos))

        output = []
        if pos is None:
            for synset in synsets:
                output.append(self._prepare_entry(synset.definition(), ProcessedWord(synset.name())))
        else:
            for synset in synsets:
                processed_word = ProcessedWord(synset.name())
                if processed_word.is_part_of_speech(pos):
                    output.append(self._prepare_entry(synset.definition(), processed_word))

        if not similar:
            output = list(filter(lambda item: item['word'].raw_word() == word, output))

        return output

    def _prepare_entry(self, definition, processed_word):
        return {'definition': definition, 'word': processed_word}
