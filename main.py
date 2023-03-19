import requests
from send_email import send_email


api_key = "439e692d12e842e1b5e840e98f2a971c"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-02-19&sortBy=publishedAt&apiKey" \
    "=439e692d12e842e1b5e840e98f2a971c"
request = requests.get(url)
content = request.json()
body = ""
for article in content["articles"]:

    body = body + "Article:" + "\n" + "_______________" + "\n" + article["title"] + "\n" + \
           "Description:" + "\n" + "________________" + "\n" + article["description"] + 4*"\n"


send_email(body.encode('utf-8'))
