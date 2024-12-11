from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    try:
        content = requests.get(url).text
        soup = BeautifulSoup(content, 'html.parser')
        rate = soup.find("span", class_="ccOutputRslt").get_text()
        rate = float(rate[:-4])  # Remove currency symbol
        return rate
    except Exception as e:
        print(f"Error fetching currency rate: {e}")
        return None

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1> Currency Rate API </h1> <p>Example URL: /api/v1/eur-usd</p>'

@app.route('/api/v1/<in_cur>-<out_cur>')
def api(in_cur, out_cur):
    rate = get_currency(in_cur, out_cur)
    if rate is None:
        return jsonify({'error': 'Unable to fetch currency rate'}), 500

    result_dictionary = {'input_currency': in_cur, 'output_currency': out_cur, 'rate': rate}
    return jsonify(result_dictionary)

if __name__ == '__main__':
    app.run(debug=True)
