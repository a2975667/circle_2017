import random
import nltk
#from nltk import word_tokenize, trigrams
from collections import defaultdict

cleanse_dict = {
            "ain't": "am not",
            "aren't": "are not",
            "can't": "cannot",
            "can't've": "cannot have",
            "'cause": "because",
            "could've": "could have",
            "couldn't": "could not",
            "couldn't've": "could not have",
            "didn't": "did not",
            "doesn't": "does not",
            "don't": "do not",
            "hadn't": "had not",
            "hadn't've": "had not have",
            "hasn't": "has not",
            "haven't": "have not",
            "he'd": "he would",
            "he'd've": "he would have",
            "he'll": "he will",
            "he'll've": "he will have",
            "he's": "he is",
            "how'd": "how did",
            "how'd'y": "how do you",
            "how'll": "how will",
            "how's": "how is",
            "I'd": "I would",
            "I'd've": "I would have",
            "I'll": "I will",
            "I'll've": "I will have",
            "I'm": "I am",
            "I've": "I have",
            "isn't": "is not",
            "it'd": "it would",
            "it'd've": "it would have",
            "it'll": "it will",
            "it'll've": "it will have",
            "it's": "it is",
            "let's": "let us",
            "ma'am": "madam",
            "mayn't": "may not",
            "might've": "might have",
            "mightn't": "might not",
            "mightn't've": "might not have",
            "must've": "must have",
            "mustn't": "must not",
            "mustn't've": "must not have",
            "needn't": "need not",
            "needn't've": "need not have",
            "o'clock": "of the clock",
            "oughtn't": "ought not",
            "oughtn't've": "ought not have",
            "shan't": "shall not",
            "sha'n't": "shall not",
            "shan't've": "shall not have",
            "she'd": "she would",
            "she'd've": "she would have",
            "she'll": "she will",
            "she'll've": "she will have",
            "she's": "she is",
            "should've": "should have",
            "shouldn't": "should not",
            "shouldn't've": "should not have",
            "so've": "so have",
            "so's": "so as",
            "that'd": "that would",
            "that'd've": "that would have",
            "that's": "that is",
            "there'd": "there would",
            "there'd've": "there would have",
            "there's": "there is",
            "they'd": "they would",
            "they'd've": "they would have",
            "they'll": "they will",
            "they'll've": "they will have",
            "they're": "they are",
            "they've": "they have",
            "to've": "to have",
            "wasn't": "was not",
            "we'd": "we would",
            "we'd've": "we would have",
            "we'll": "we will",
            "we'll've": "we will have",
            "we're": "we are",
            "we've": "we have",
            "weren't": "were not",
            "what'll": "what will",
            "what'll've": "what will have",
            "what're": "what are",
            "what's": "what is",
            "what've": "what have",
            "when's": "when is",
            "when've": "when have",
            "where'd": "where did",
            "where's": "where is",
            "where've": "where have",
            "who'll": "who will",
            "who'll've": "who will have",
            "who's": "who is",
            "who've": "who have",
            "why's": "why is",
            "why've": "why have",
            "will've": "will have",
            "won't": "will not",
            "won't've": "will not have",
            "would've": "would have",
            "wouldn't": "would not",
            "wouldn't've": "would not have",
            "y'all": "you all",
            "y'all'd": "you all would",
            "y'all'd've": "you all would have",
            "y'all're": "you all are",
            "y'all've": "you all have",
            "you'd": "you would",
            "you'd've": "you would have",
            "you'll": "you will",
            "you'll've": "you will have",
            "you're": "you are",
            "you've": "you have",
            ":": "",
            "(": "",
            ")": "",
            "/": "",
            "&": "",
}

def pre_processing(words):
    """converts contractions to real words"""
    result = []
    for word in words:
        if word not in cleanse_dict.keys():
            result.append(word)
        else:
            result.append(cleanse_dict[word])
    return result


def clean_data(path):
    with open(path, 'r') as f:      #讀入檔案
        raw_text = f.read()

    words = raw_text.split()        #切割為文字
    words = pre_processing(words)   #處理縮寫
    text = " ".join(words)          #復原
    #print(text[-150:])
    words = nltk.word_tokenize(text)     #使用nltk
    #print ("-----------")
    #print((" ".join(words))[-150:])
    return words

def get_bigram_list(words):
    bigram = nltk.bigrams(words)
    grams = []
    for gram in bigram:
        grams.append(gram)
    return grams

def get_trigram_list(words):
    trigram = nltk.trigrams(words)
    grams = []
    for gram in trigram:
        grams.append(gram)
    return grams

def create_sent(transition, starting_word):
    current = random.choice(starting_word)
    prev = "."
    result = [current]
    while True:
        next_word_candidates = transition[(prev, current)]
        next = random.choice(next_word_candidates)

        prev, current = current, next
        result.append(current)

        if current == ".":
            return " ".join(result)


if __name__ == "__main__":

    ###cleaning and processing data###
    path = "text.txt"
    words = clean_data(path)
    grams = get_trigram_list(words)
    
    ''' #(bi)
    grams = get_bigram_list(words)
    transition = defaultdict(list)
    starting_word = []
    for cur, nex in grams:
        if cur == ".":
            starting_word.append(nex)
        
        transition[cur].append(nex)      #是dictionary append!
    '''

    ###creating the data###
    transition = defaultdict(list)
    starting_word = []
    for pre, cur, nex in grams:
        if pre == ".":
            starting_word.append(cur)
        
        transition[(pre, cur)].append(nex)      #是dictionary append!
    #######################

    sentence = create_sent(transition, starting_word)
    sentence = sentence.replace(" .", ". ").replace(" ,", ",") \
               .replace(" ?", "?").replace(" n't", "n't") \
               .replace(" 's", "'s").replace(" 'd", "'d") \
               .replace(" ''", "").replace(" ..", "...")

    print (sentence)
