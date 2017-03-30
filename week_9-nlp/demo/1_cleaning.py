from text_cleaning import cleanse_dict
import random
from nltk import word_tokenize, trigrams
from collections import defaultdict

def clean_data(path):
    with open(path, 'r') as f:      #讀入檔案
        raw_text = f.read()

    words = raw_text.split()        #切割為文字
    return words



if __name__ == "__main__":
    path = "text.txt"
    words = clean_data(path)
    #print (words)

    paragraph = ""
    for j in range(random.randrange(4, 20)):
        text = ""
        for i in range(random.randrange(3, 7)):                    #隨機長度
            random_word = words[random.randrange(0,len(words))]     #隨機單字
            if (random_word != '.'):
                text += ( random_word + " ")                        
        paragraph += (text.capitalize()[:-1] + ". ")
    
    print (paragraph)