class DefinitionResponseBuilder(object):
    def __init__(self, word, result_set, pos=None):
        mapped_collection = list(map(lambda el: {
            'definition': el['definition'].capitalize(),
            'word': el['word'].word(),
            'partOfSpeech': el['word'].part_of_speech()
        }, result_set))

        self._output = {
            'word': word.replace('_', ' '),
            'results': mapped_collection,
        }
        if pos is not None:
            self._output['partOfSpeech'] = pos

    def build(self):
        return self._output
