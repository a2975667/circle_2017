import requests
from datetime import datetime
import time

res = requests.get("http://www.hko.gov.hk/wxinfo/currwx/current.htm") #res is a response object
tmp = res.text.split("The air temperatures at other places were:")[1].split('<SPAN')[1:-1]

while(1):
    data = []
    for i in tmp:
        dic = {}
        #print (i.split(">")[2].split('&'))
        #print (i.split(">")[2].strip().split('&'))
        dic['location'] = (i.split(">")[1].split('</SPAN')[0])
        dic['tmp'] = (i.split(">")[2].strip().split('&')[0])
        data.append(dic)

    print (datetime.now())
    for d in data:
        print(d['location'] + " : " + dic['tmp'], end=' ')
    
    print ("\n\n")
    time.sleep(10)