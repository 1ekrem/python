from urllib.request import urlopen
import json
import pandas
from pandas.io.json import json_normalize

def get_jsonparsed_data(url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

url = ("https://financialmodelingprep.com/api/v3/discounted-cash-flow/AAPL?apikey=bbf66c10187326f9b777ad3ff0d0c9d1")
print(get_jsonparsed_data(url))


