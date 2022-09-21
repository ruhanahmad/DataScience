from lib2to3.pgen2 import driver
from turtle import title
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from selenium.webdriver.common.by import By
import pandas as pd
import os
import json
from datetime import date
import mail
import smtplib




SENDER_EMAIL = 'ranaruhan123@gmail.com'
RECEIVER_EMAIL = 'zumranoor09@gmail.com'
today = str(date.today()) + ".csv"
def send_email():
  s = smtplib.SMTP('smtp.gmail.com', 587)
  s.starttls()
  s.login(SENDER_EMAIL, 'seleniumworkshop')
  message = "This is a message from AWS Lambda"
  s.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message)
  s.quit()








def get_trend():
  driver = webdriver.Chrome(executable_path='D:\\Selenium\\chromedriver.exe')


  Youtube_Url = "https://www.youtube.com/feed/trending"
  driver.get(Youtube_Url)
  print(driver.title)
  video_div_classes = "ytd-video-renderer"
  video_divs = driver.find_elements(By.TAG_NAME,video_div_classes)

# response = requests.get(Youtube_Url)

# # with open('trending.html','w') as f:
# #      f.write(response.text)

# doc = BeautifulSoup(response.text,'html.parser')

# video_divs =doc.find_all("div", class_= "ytd-video-renderer",)

  print(len(video_divs))
  return video_divs
get_trend()
video =get_trend()


def fetch_all(videos):

   tital_tag = videos.find_element(By.ID,"video-title")

   tital = tital_tag.text

   Url = tital_tag.get_attribute('href')

   Thumbnail_url = videos.find_element(By.TAG_NAME,'img').get_attribute('src')
   channel_name =  videos.find_element(By.CLASS_NAME,'style-scope ytd-channel-name')
   views =  videos.find_element(By.ID,'metadata-line')
   return {
    'title' : tital,
    'Url':Url,
    'ThumbnailUrl' : Thumbnail_url,
    'channel_name' : channel_name,
    'title' : tital,
    'channel_name':channel_name,
    'viewsAndLikes':views

   }

all_Data=[fetch_all(videos) for videos in video[:10]]
print(all_Data)


mail.send(filename=today)

# CSV_V = pd.DataFrame(all_Data)
# CSV_V.to_csv(today)




