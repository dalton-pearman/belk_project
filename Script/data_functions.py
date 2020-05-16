import pandas as pd
import requests

""""
This code will pull the three finacial statements based on a ticker input
The results are in the form of a dictornary comprised of three data frames
To accress run df = grab_statments(ticker)
df['income-statement'] for income statement
df['balance-sheet-statement'] for balance sheet
df['cash-flow-statement'] for cash flow statement

"""""


def grab_statements(ticker):
    names = ['income-statement', 'balance-sheet-statement', 'cash-flow-statement']
    holder = {}
    for i in names:
        try:
            req = requests.get('https://financialmodelingprep.com/api/v3/financials/'+i+'/'+ticker)
            holder[i] = pd.io.json.json_normalize(req.json(), record_path='financials')
        except KeyError:
            print("Invalid ticker symbol \nPlease enter correct ticker")
            break
    return holder
