import requests

api_key = "439e692d12e842e1b5e840e98f2a971c"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-02-19&sortBy=publishedAt&apiKey" \
    "=439e692d12e842e1b5e840e98f2a971c"
request = requests.get(url)
content = request.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"])

