
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')


from bs4 import BeautifulSoup
import pandas as pd
import re
import datetime
import requests
import time


n = 1
df = pd.DataFrame()
column_names =['Title','Stars','DateTime']
while True:
  print(n)
  if n == 951:
    False
    break
  else:
    n = n + 1

  base_url = 'https://www.theguardian.com/film+tone/reviews?page='+str(n)
  
  try:
    driver = webdriver.Chrome('chromedriver',options=options)
    #print("driver loaded!")
  except:
    print("driver did not load")
    break

  driver.get(base_url)


  page = driver.page_source
  soup = BeautifulSoup(page, 'html.parser')
  items = list(soup.find_all("li",class_="fc-slice__item"))

  #print(len(items))
  """
  if len(items) == 0:
      nao = 1
      False
      break
  else:
      n = n + 1
  """

  data=[] 
  for item in items:
    
    title = item.find(class_="js-headline-text")
    try:
        title = title.get_text()
    except:
        title = "" 

    stars = item.find(class_="u-h")
    try:
        stars = stars.get_text()
    except:
        stars = "" 

    try:
        date_time = item.time.get("datetime")
    except:
        date_time = ""


    #print(title + ' - ' + stars)
    stuff = [title,stars,date_time]
    data.append(stuff)

  #print(data)
  df = df.append(data,ignore_index=True)

df.columns = column_names

file_name = 'Guardian-FilmReview-950.csv'
df.to_csv(file_name,index=False)

