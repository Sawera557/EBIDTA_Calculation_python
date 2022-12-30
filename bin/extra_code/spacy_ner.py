# pip install spacy
# python -m spacy download en_core_web_sm

import spacy
nlp = spacy.load("en_core_web_sm")  # load the pre-trained model

import pandas as pd




def match_Qualified_Data(name, path):
    df = pd.read_excel(path)
    entities = []

    balance = ['assets', 'liabilities', 'equity']
    income = ['revenues','expense','profit','income']
    cashflow = ['inflows','outflows','operating','investing','financing']


    for index, row in df.iterrows():
        text = str(row["Assets"])  # extract the text from the relevant column
        doc = nlp(text)  # create a spacy document
        for entity in doc.ents:
            if not entity.text=="" and not entity.text=="nan":
                entities.append((entity.text, entity.label_))  # extract the entities and their labels




    print(entities)

path = "../finance_data/Balance.xlsx"
match_Qualified_Data(path)