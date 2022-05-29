from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import webtext
from nltk.probability import FreqDist
import nltk
import matplotlib.pyplot as plt
nltk.download('punkt')

word=open("/Users/apple/Desktop/code/python projects/words.py/words.txt","r")
lofwords=[word.read()]

 
def listToString(s): 
    str1 = "" 
    for ele in s: 
        str1 += ele  
    return str1 
    
s=listToString(lofwords)

words = nltk.word_tokenize(s)

words=[word.lower() for word in words if word.isalpha()]
print(words)   


for i in range(len(sorted(words))):
    print("%s: %s" % (i, words[i]))
 
data_analysis = nltk.FreqDist(words)

data_analysis.plot(25, cumulative=False)