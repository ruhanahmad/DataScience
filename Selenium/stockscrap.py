from email import header
from gettext import find
import requests
import time
from bs4 import BeautifulSoup
import csv
Urls = ["https://finance.yahoo.com/quote/GOOG/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAAaRicg9Sp8fjA9ekz9Ik3i_LBI4V50xUvEWVBKYK2a4IOaFFOBfL_rtAA6aq3BYchnPuHBzRreeujKqDmPwASdxmShaO2KIvZwy31sWuocvnlRa-QGeFl8Nm3kKWRvTXnK3cFsYAOEy037uNj8FSq-kziCCVCqKsHks1E01NAcK","https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch","https://finance.yahoo.com/quote/APLE?p=APLE&.tsrc=fin-srch"]
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

csv_file = open("scrap.csv","w")
csv_writer = csv.writer(csv_file)


for url in Urls:
 html_page = requests.get(url,headers=headers)

 soup = BeautifulSoup(html_page.content,'lxml')
 header_info = soup.find_all("div", id="quote-header-info")[0]
 stock_title = header_info.find("h1").get_text()
 current_price = header_info.find("div", class_="My(6px) Pos(r) smartphone_Mt(6px) W(100%)").find("fin-streamer").get_text()


 header_info_two = soup.find_all("div", class_="D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)")[0].find_all("table",class_="W(100%)")[0].find_all("tbody")[0].find_all("tr")
# table_content_one = header_info_two.find_all("td")[0].get_text()
# table_content_two = header_info_two.find_all("td")[1].get_text()
# current_chart = header_info_two.find_all("div",class_="Ta(end) Fw(600) Lh(14px)").get_text()


# current_price_two = header_info_two.find("td", class_="C($primaryColor) W(51%)").find("span").get_text()

 for i in range(0,2):
  table_content_one = header_info_two[i].find_all("td")[0].get_text()
  table_content_two = header_info_two[i].find_all("td")[1].get_text()
  
  print(table_content_one + ": " + table_content_two)

# print(header_info_two)



