import requests
import os
from dotenv import load_dotenv

load_dotenv()

my_api_key = os.environ.get('API_KEY')
 


# r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2022-2-27&to=2022-2-28&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c')
# content = r.json()

# articles = content['articles']
# print(type(articles))

# for article in articles:
#     print("Title: " + article['title'], "Description: " + article['description']);

def get_News(country):
    api_key = my_api_key
    url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={my_api_key}"
    r = requests.get(url)
    content = r.json()
    print(content)
    articles = content["articles"]
    result = []
    for article in articles:
        result.append(f"Title: {article['title']} Description: {article['description']}")
    return result

print(get_News(country="us"))




