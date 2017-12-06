import nltk
import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

def string_to_array(input):
    input = str(input)
    words = []
    lemmatizer = WordNetLemmatizer()
    stop_words = generate_stopwords()

    tokenized = nltk.word_tokenize(input) # split to words
    tokenized_filtered = [w for w in tokenized if not w in stop_words] # filter out all stop words (I, have, we, is, ...)

    for word in tokenized_filtered:
        words.append(lemmatizer.lemmatize(word.lower()))

    return words, len(words)

def generate_stopwords():
    result = stopwords.words('english')
    result += ['(', ')', '\'s', '\'ve', '\'re', '\'m']
    
    return set(result)

def remove_urls(str):
    str = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', str)
    
    return str

def map_strings(str):
    str = remove_urls(str)
    lines = str.split('|||')
    words = []
    
    for l in lines:
        stats = string_to_array(l)
        
        words = list(set(words + stats[0]))
        
    return words, len(words)
