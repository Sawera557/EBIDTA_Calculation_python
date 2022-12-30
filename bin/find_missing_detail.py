from bin.match_words import match_keywords
from bin.nltk_NER import extract_entities

def find_missing_values(file_name, path):

    entities = extract_entities(path)
    response = match_keywords(file_name, entities)
    return response


