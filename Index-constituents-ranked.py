# I Hussain 24-2-23
# This module will list an index by past year growth performance. 
# It is a work in progress and will need to be integrated to the main program when finished.

import requests
from bs4 import BeautifulSoup

url = "https://au.finance.yahoo.com/quote/%5EAFLI/components?p=%5EAFLI"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

symbol_table = soup.find('table', attrs={'class': 'W(100%) M(0) BdB Bdc($tableBorderGray)'})
if symbol_table is None:
    print("Table not found on the webpage")
    symbols = []
else:
    symbol_rows = symbol_table.find_all('tr')[1:]
    symbols = []
    for row in symbol_rows:
        symbol = row.find_all('td')[0].text.strip()
        symbols.append(symbol)

print(symbols)