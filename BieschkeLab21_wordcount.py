#BieschkeLab21: word count 
'''
Open the file.
Make everything lowercase, strip punctuation, split into a list of words.

To strip punctuation:
import string
s = 'I $am a !string with punc&^%*tuation!'
translator = str.maketrans('', '', string.punctuation)
string_without_punct = s.translate(translator) # I am a string with punctuation

Your dictionary will have words as keys and counts as values. 
If a word isn't in your dictionary yet, add it with a count of 1. 
If it is, increment its count.

Print the most frequent top 10 out with their counts. You can do that with the code below.
# word_dict is a dictionary where the key is the word and the value is the count
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])

You'll find that the most common words aren't particularly interesting (lots of 'I's, 'the', 'and', 'he', 'she', and 'but's). 
To get more relevant words, remove stop words from your text.
'''
stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

import string
counts = {}

with open("dunwich_horror.txt", "r") as file:
    data = file.read().replace('\n', ' ')
    translator = str.maketrans('', '', string.punctuation)  
    data_wo_punct = data.translate(translator) 
    text = data_wo_punct.lower()
    text2 = text.split(' ')
    
    go_words = [word for word in text2 if word not in stopwords]    #utilizes stopwords

    for word in go_words:
        if word in counts:
            counts[word] +=1
        else:
            counts[word] = 1
            #added = dict(zip(word, ))
    print(counts)

    words = list(counts.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])

    #print(text2)