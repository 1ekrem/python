def build_person(first_name, last_name):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name }
    return person

musician = build_person('Ekrem', 'Ersayin')
print(musician)


def build_ticker(ticker, marketName, publishDate=''):
    """Return the index of a ticker"""
    tick = {'ticker': ticker, 'market':marketName}
    if publishDate:
        tick['publishDate'] = publishDate
    return tick

stockAnalysis = build_ticker('TSLA','NASDAQ', publishDate=2005)
print(stockAnalysis)

stockAnalysis2 = build_ticker('TSLA','NASDAQ')
print(stockAnalysis2)
