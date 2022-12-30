from flask import Flask, request, jsonify

from bin.calculate_ebidta import get_values_from_files
from bin.find_missing_detail import find_missing_values

app = Flask(__name__)

def calculate_ebitda(net_income, tot_expenxe, taxes, depreciation_amortization):
    ebitda = float(net_income) - float(tot_expenxe) - float(taxes) - float(depreciation_amortization)
    return ebitda


@app.route('/calculate_ebitda', methods=['POST'])
def calculate_ebitda01():

  # Get the uploaded documents from the request
  balance_sheet = request.files['balance_sheet']
  income_statement = request.files['income_statement']
  cash_flow_statement = request.files['cash_flow_statement']

  #balance_sheet = "finance_data/Balance.xlsx"
  #income_statement = "finance_data/income.xlsx"
  #cash_flow_statement = "finance_data/cashflow.xlsx"

  finance_files = [{"file_path":balance_sheet,"filename":"balance"},{"file_path":income_statement,"filename":"income"},{"file_path":cash_flow_statement,"filename":"cashflow"}]
  miss_vals = []
  for i in finance_files:
    file_path = i["file_path"]
    filename = i["filename"]
    response = find_missing_values(filename, file_path)
    miss_vals.append(response)
  for res in miss_vals:
      if res["status"] == False:
          return miss_vals
      else:
          all_values = get_values_from_files(finance_files)
          print(all_values)
          tot_expenxe = all_values[0]['tot_expenxe']
          in_tax = all_values[0]['in_tax']
          dep_amor = all_values[0]['dep_amor']
          net_value = all_values[0]['net_value']

          ebitda = calculate_ebitda(net_value, tot_expenxe, in_tax, dep_amor)

          print("ebidta is: ",ebitda)

          # Return the EBITDA to the user
          return jsonify({'ebitda': ebitda})

if __name__ == '__main__':
  app.run(debug=True)
