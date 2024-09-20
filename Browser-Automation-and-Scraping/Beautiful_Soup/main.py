from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency, user_amount):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount={user_amount}"
    requested_Info = requests.get(url).text

    # When using Beautiful soup you need a parse fot he 2nd argument. the one we are using ins html.parser. Also note that the [4:] will take away the first characters of the string and [:-4] will take away the last 4 characters of the string value
    soup = BeautifulSoup(requested_Info, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt" ).get_text()
    rate = float(rate[:-4].replace(',', ''))
    return rate

print(get_currency("USD", "COP", 100))