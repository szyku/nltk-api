class TaggerResponseBuilder(object):
    def __init__(self, input_elements, result_set):
        self._outputCollection = []
        self._outputRoot = {'input': input_elements}
        self._prepare_result_items(result_set)

    def build(self):
        self._outputRoot['results'] = self._outputCollection
        return self._outputRoot

    def _create_item(self, word, pos):
        return {'item': word, 'partOfSpeech': pos}

    def _prepare_result_items(self, result_set):
        for sentence_collection in result_set:
            sentence_processed = []
            for meta in sentence_collection:
                sentence_processed.append(self._create_item(meta[0], meta[1]))
            self._outputCollection.append(sentence_processed)
