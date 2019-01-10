'''
1-Go to wikipedia for the SP500 companies,
2-pull all the tickers
'''
import pickle
import requests
import bs4 as bs


def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, "lxml")
    table = soup.find('table', {'class' : 'wikitable sortable'})
    tickers= []

    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        mapping = str.maketrans(".","-")
        ticker = ticker.translate(mapping)
        tickers.append(ticker)

    with open("sp500tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)
    
    print(tickers)
    return tickers

save_sp500_tickers()