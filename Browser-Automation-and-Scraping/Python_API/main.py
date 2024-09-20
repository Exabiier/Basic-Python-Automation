import requests

# Because the the market watch API is not free I must us the following. Stils need solution for bringing mutliple cvs data into one data format
#  Just like Java you canvert data types in python with datatype() -> int()
# picker = input('Enter the stock symbol you want:')
from_date = input('Enter Start data in mm/dd/yyyy format:')
to_date = input('Enter end data in mm/dd/yyyy format:')


url = f"https://www.marketwatch.com/investing/stock/csv/downloaddatapartial?startdate={from_date}%2000:00:00&enddate={to_date}%2000:00:00&daterange=d30&frequency=p1d&csvdownload=true&downloadpartial=false&newdates=false"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.marketwatch.com/"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    content = respnonse.content
    print(content)
    with open('data.csv', 'wb') as file:
        file.write(content)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")



