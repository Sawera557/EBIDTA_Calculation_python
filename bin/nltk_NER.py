# pip install nltk

from nltk import word_tokenize, pos_tag, ne_chunk
import nltk
from bin.get_all_excel_text import get_all_excel_text

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

import pandas as pd

def extract_ne_text(tree):
    text = ""
    for subtree in tree:
        if isinstance(subtree, nltk.tree.Tree):
            label = subtree.label()
            text += label + " "
            for leaf in subtree:
                text += leaf[0] + " "
        else:
            text += subtree[0] + " "
    return text.strip()


def extract_entities(path):
    all_data = get_all_excel_text(path)

    all_entities = []
    for keyword in all_data:
        text = str(keyword.lower())  # extract the text from the relevant column
        tokens = word_tokenize(text)  # tokenize the text
        tagged_tokens = pos_tag(tokens)  # tag the tokens with part-of-speech tags
        named_entities = ne_chunk(tagged_tokens)  # extract named entities
        if not named_entities=="nan":
            text = extract_ne_text(named_entities)
            all_entities.append(text)  # you can do something with the named entities here
    return all_entities



"""
import files 
get all text data from excel files
get all ner entities
match all data
"""