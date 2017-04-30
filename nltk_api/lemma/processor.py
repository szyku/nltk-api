from nltk import WordNetLemmatizer
from nltk.corpus.reader import NOUN, VERB, ADJ, ADV

POS = {
    'noun': NOUN,
    'verb': VERB,
    'adjective': ADJ,
    'adverb': ADV,
}


def assert_correct_format(candidate):
    if not isinstance(candidate, dict):
        raise TypeError('The value should ba dictionary.')
    if 'word' not in candidate or 'type' not in candidate:
        raise KeyError('Mandatory keys are missing. Expecting word and type keys.')


class LemmaProcessor(object):
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()

    def lemma(self, word='', word_type_str=''):
        pos = POS.get(word_type_str, None)
        final_type = word_type_str
        if pos is None:
            pos = NOUN
            final_type = 'noun'

        return {"lemma": self.lemmatizer.lemmatize(word, pos), "type": final_type}

    def all_lemma(self, word=''):
        output = []
        for word_type_str, val in POS.items():
            output.append(self.lemma(word, word_type_str))

        return output
