from nltk.corpus.reader.wordnet import NOUN, VERB, ADJ, ADJ_SAT, ADV

IDX_WORD, IDX_POS, IDX_SEQ = 0, 1, 2

REVERSE_POS = {
    NOUN: 'noun',
    VERB: 'verb',
    ADJ: 'adjective',
    ADJ_SAT: 'adjective',
    ADV: 'adverb',

}


class ProcessedWord(object):
    def __init__(self, sysnet_word):
        if not isinstance(sysnet_word, str):
            raise TypeError('Constructor expects string argument.')

        tokens = sysnet_word.split('.')

        if not len(tokens) == 3:
            raise ValueError('The word should contain two dots separating meta information <lemma>.<pos>.<number>')

        self._word_raw = tokens[IDX_WORD]
        self._pos_raw = tokens[IDX_POS]
        self._index = int(tokens[IDX_SEQ])

        self._normalized_word = self._word_raw.replace("_", " ")
        self._pos = REVERSE_POS.get(self._pos_raw)
        self._original_word = sysnet_word

    def raw_word(self):
        return self._word_raw

    def word(self):
        """
        Return human readable representation of the word
        :return:
        """
        return self._normalized_word

    def part_of_speech(self):
        return self._pos

    def raw_part_of_speech(self):
        return self._pos_raw

    def word_index(self):
        return self._index

    def is_part_of_speech(self, pos):
        if isinstance(pos, str) and len(pos) == 1:
            return self._pos_raw == pos

        if isinstance(pos, str):
            return self._pos == pos

        raise TypeError("Cannot check part of speech with provided argument.")

    def __str__(self):
        return "Word: %s, part of speech: %s".format(self._normalized_word, self._pos)
