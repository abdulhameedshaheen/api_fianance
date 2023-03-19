import requests
from send_email import send_email

topic ="tesla"
api_key = "439e692d12e842e1b5e840e98f2a971c"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-02-19&" \
      "sortBy=publishedAt&" \
      "apiKey=439e692d12e842e1b5e840e98f2a971c&" \
      "language=en"
request = requests.get(url)
content = request.json()
body = ""
for article in content["articles"][:20]:

    body = "Subject: Todays News" +"\n" + body + " Article:" + "\n" + "_______________" + "\n" + article["title"] + "\n" + \
           "Description:" + "\n" + "________________" + "\n"\
           + article["description"] + "\n" + article["url"] + 4*"\n"


send_email(body.encode('utf-8'))
