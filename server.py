from flask import Flask, render_template
import requests

app = Flask(__name__)
API_URL = 'https://financialmodelingprep.com/api/v3/stock/real-time-price/{}'


def fetch_price(ticker):
    """Sends a HTTP request to an API provided by financialmodelingprep.com


    Args:
        ticker: a string parameter to render just the price of a single stock


    Returns: the price of the stock as a JSON object
    """
    data = requests.get(API_URL.format(ticker.upper()), params={'apikey': 'demo'}).json()
    return data["price"]


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/stocks/<string:ticker>')
def view_stock(ticker):
    stock_price = fetch_price(ticker)
    return render_template('stock_quote.html', ticker = ticker, stock_price = stock_price)
