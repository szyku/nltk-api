class LemmaResponseBuilder(object):
    def __init__(self):
        self._outputCollection = []
        self._outputRoot = {}
        pass

    def add_entry(self, word, result):
        self._outputCollection.append({"word": word, "result": result})

    def add_query(self, query):
        self._outputRoot['query'] = query

    def build(self):
        self._outputRoot['results'] = self._outputCollection
        return self._outputRoot
