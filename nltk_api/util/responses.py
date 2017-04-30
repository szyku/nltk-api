from werkzeug.exceptions import BadRequest

from nltk_api.lemma.processor import POS


class BadRequestIncorrectPos(BadRequest):
    description = "Incorrect POS. Use one of these values: " + ", ".join(POS.keys()) + " or omit the value."
