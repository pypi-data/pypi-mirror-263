from nltk.corpus import wordnet as wn
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

mapper = {'CC': None,
           'CD': wn.NOUN,
           'DT': wn.NOUN, #None
           'EX': wn.ADV,
           'FW': wn.NOUN, #None
           'IN': wn.ADV,
           'JJ': [wn.ADJ, wn.ADJ_SAT],
           'JJR': [wn.ADJ, wn.ADJ_SAT],
           'JJS': [wn.ADJ, wn.ADJ_SAT],
           'LS': wn.NOUN, #None
           'MD': wn.NOUN, #None
           'NN': wn.NOUN,
           'NNS': wn.NOUN,
           'NNP': wn.NOUN,
           'NNPS': wn.NOUN,
           'PDT': [wn.ADJ, wn.ADJ_SAT],
           'POS': wn.NOUN, #None
           'PRP': wn.NOUN, #None
           'PRP$': wn.NOUN, #None
           'RB': wn.ADV,
           'RBR': wn.ADV,
           'RBS': wn.ADV,
           'RP': [wn.ADJ, wn.ADJ_SAT],
           'SYM': wn.NOUN, #None
           'TO': wn.NOUN, #None
           'UH': wn.NOUN, #None
           'VB': wn.VERB,
           'VBD': wn.VERB,
           'VBG': wn.VERB,
           'VBN': wn.VERB,
           'VBP': wn.VERB,
           'VBZ': wn.VERB
           }

def WordBank(text):

  token = word_tokenize(text)

  tags = pos_tag(token)
  w_net_lemma = []

  for tag in tags:
    poos = mapper[tag[1]]
    try:
      if (len(poos) > 1):
        poos = poos[0]
    except:
      pass

    w_net_lemma.append(WordNetLemmatizer().lemmatize(tag[0], pos=poos))

  return w_net_lemma
