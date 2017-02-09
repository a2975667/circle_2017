#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url= 'http://www.books.com.tw/web/books_bmidm_0102/?o=1&v=2&page=1'
html = requests.get(url)
html.encoding="utf-8"

sp = BeautifulSoup(html.text, 'html.parser')


items = sp.find("div", {"class":"wrap"})
titles = items.find_all("h4")
prices = items.find_all("li", {"class":"set2"})
authors = items.find_all("li", {"class":"info"})


print titles[0]

