from nltk import pos_tag_sents as tagger
from nltk import word_tokenize as tokenizer
POS_TAGS = {
    '$': 'dollar',
    "''": 'quote_close',
    '(': 'parenthesis_open',
    ')': 'parenthesis_close',
    ',': 'comma',
    '--': 'dash',
    '.': 'terminator',
    ':': 'colon_ellipsis',
    'CC': 'conj_coordinating',
    'CD': 'numeral_cardinal',
    'DT': 'determiner',
    'EX': 'existential_there',
    'FW': 'foreign word',
    'IN': 'prep_or_conj_subordinating',
    'JJ': 'adj_or_numeral_ordinal',
    'JJR': 'adj_comparative',
    'JJS': 'adj_superlative',
    'LS': 'list_item_marker',
    'MD': 'modal_aux',
    'NN': 'noun_comm_sing_or_mass',
    'NNP': 'noun_proper_sing',
    'NNPS': 'noun_proper_pl',
    'NNS': 'noun_comm_pl',
    'PDT': 'pre-determiner',
    'POS': 'genitive_marker',
    'PRP': 'pronoun_personal',
    'PRP$': 'pronoun_possessive',
    'RB': 'adverb',
    'RBR': 'adverb_comparative',
    'RBS': 'adverb_superlative',
    'RP': 'particle',
    'SYM': 'symbol',
    'TO': 'to_infi_pre',
    'UH': 'interjection',
    'VB': 'verb_base',
    'VBD': 'verb_past',
    'VBG': 'verb_present',
    'VBN': 'verb_past_parti',
    'VBP': 'verb_present_not_3rd_person',
    'VBZ': 'verb_present_3rd_person',
    'WDT': 'wh-determiner',
    'WP': 'wh-pronoun',
    'WP$': 'wh-pronoun_possessive',
    'WRB': 'wh-adverb',
    '``': 'quote_open'
}
_IDX_WORD, _IDX_SYMBOL = 0, 1


def tag_sentences(sentences, pos_symbol=False):
    tokenized = []
    for sent in sentences:
        tokenized.append(tokenizer(sent))

    processed_list = tagger(tokenized)

    if not pos_symbol:
        output_list = []
        for sentence in processed_list:
            new_sentence = []
            for word in sentence:
                new_sentence.append((word[_IDX_WORD], POS_TAGS[word[_IDX_SYMBOL]]))
            output_list.append(new_sentence)
    else:
        output_list = processed_list

    return output_list
