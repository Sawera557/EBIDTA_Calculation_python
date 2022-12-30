
def match_keywords(filename, entities):
    balance = ['assets', 'liabilities', 'equity', 'taxes', 'income']
    income = ['revenue', 'total', 'expenses', 'cost', 'profit', 'income']
    cashflow = ['operating activities', 'net', 'amortization', 'Depreciation', 'investing acitivies', 'financing activities']

    if filename=="income":
        found = True
        element = []
        for i in income:
             for en in entities:
                 if i in en.lower():
                     break
             else:
                element.append(i)
                found==False

    elif filename=="balance":
        found = True
        element = []
        for i in balance:
            for en in entities:
                if i in en.lower():
                    break
            else:
                element.append(i)
                found == False

    elif filename=="cashflow":
        found = True
        element = []
        for i in cashflow:
            for en in entities:
                if i in en.lower():
                    break
            else:
                element.append(i)
                found == False

    result = []

    if len(element)==1:
        result.append({"filename":filename,"status":found, "response": f"{filename} sheet is missing {element} column"})
    elif len(element)==1:
        result = {"filename": filename, "status": found, "response": f"{filename} sheet is missing {element} column"}
    elif element==[]:
        result = {"filename": filename, "status": found, "response": f"{filename} sheet has all the important information!"}


    return result