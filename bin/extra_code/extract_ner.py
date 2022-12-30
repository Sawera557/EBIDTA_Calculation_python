# pip install spacy
# python -m spacy download en_ner_stanford

import transformers

from bin.get_all_excel_text import get_all_excel_text

nlp = transformers.pipeline("ner", model="dslim/bert-base-NER")

def match_Qualified_Data(path):
    all_data = get_all_excel_text(path)

    output = str(" ".join(all_data))
    print(output)
    output = nlp(output)
    print("output: ",output)
    entities = []
    for i, word in enumerate(output):
        #if word['entity'] != 'O':
        entities.append((word['word'], word['entity']))
    print('Extracted named entities:', entities)


path = "../finance_data/Balance.xlsx"
match_Qualified_Data(path)