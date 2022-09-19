from urllib import response
import requests

from bs4 import BeautifulSoup
Youtube_link = "https://www.youtube.com/feed/trending"

response = requests.get(Youtube_link)
print(response.status_code)

with open("trending.html" ,'w',encoding="utf-8") as f:
 f.write(response.text)


doc = BeautifulSoup(response.text,"html.parser")
print(doc.title.text)
# print(response.text)