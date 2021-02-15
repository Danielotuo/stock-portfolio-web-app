from flask import Flask
import requests

app = Flask(__name__)


def fetch_price(ticker):
    """Sends a HTTP request to an API provided by financialmodelingprep.com


    Args:
        ticker: a string parameter to render just the price of a single stock
    

    Returns: the price of the stock as a JSON object
    """
    data = requests.get('https://financialmodelingprep.com/api/v3/stock/real-time-price/{}'.format(ticker.upper()), params={'apikey': 'demo'}).json()
    return data["price"]

@app.route('/')
def home():
    return "This is the home page. Try going to /stocks/AAPL"

@app.route('/stocks/<ticker>')
def stock(ticker):
    stock_price = fetch_price(ticker)
    return "The price of {} is {}".format(ticker, stock_price)

