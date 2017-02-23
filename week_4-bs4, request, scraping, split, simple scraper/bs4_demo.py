import requests
from bs4 import BeautifulSoup

all_books = []

#add this for loop last, just to look though the first 4 pages
for j in range(1,5):
    #PART1: get HTML response
    res = requests.get("http://www.books.com.tw/web/books_nbtopm_02/?o=1&v=1&page="+str(j)) #res is a response object
    soup = BeautifulSoup(res.text, 'html.parser') #use .text to get html and use html parser

    #this webpage has two wrap (use tool)
    #to get the first one we can get it from [0], [1] gets the second
    items = soup.select('.wrap')[0].select('.item')

    '''
    #to locate all the properties we can choose this as a template
    test = items = soup.select('.wrap')[0].select('.item')[-1]
    print ("title: " + test.select('h4')[0].text)
    print ("author: " + test.select('.info')[0].select('a')[0].text)
    print ("publisher: " + test.select('.info')[0].select('a')[1].text)
    print ("price: " + test.select('.set2')[0].select('strong')[1].text)
    '''

    #we could use book object to process this, 
    #but this would not be covered for now
    #so we would use lists
    
    for item in items:
        newBook = {}
        newBook["title"] = item.select('h4')[0].text
        newBook["author"] = item.select('.info')[0].select('a')[0].text
        newBook["publisher"] = item.select('.info')[0].select('a')[1].text
        newBook["price"] = item.select('.set2')[0].select('strong')[1].text
        all_books.append(newBook)

for book in all_books:
    print(book)
