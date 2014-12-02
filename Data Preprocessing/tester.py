'''
Created on Sep 12, 2014

@author: GAURAV
'''

import urllib
import re
import pickle
from bs4 import BeautifulSoup
from nltk.corpus import stopwords       
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import PorterStemmer
import nltk
import operator
from operator import itemgetter
from mod1 import Counter

url_list=['http://web.cse.ohio-state.edu/~srini/674/public/reuters/reut2-000.sgm',
          'http://web.cse.ohio-state.edu/~srini/674/public/reuters/reut2-001.sgm',
          'http://web.cse.ohio-state.edu/~srini/674/public/reuters/reut2-002.sgm',
          'http://web.cse.ohio-state.edu/~srini/674/public/reuters/reut2-003.sgm',
          'http://web.cse.ohio-state.edu/~srini/674/public/reuters/reut2-004.sgm',
          'http://web.cse.ohio-state.edu/~srini/674/public/reuters/reut2-005.sgm',
          'http://web.cse.ohio-state.edu/~srini/674/public/reuters/reut2-006.sgm',
          'http://web.cse.ohio-state.edu/~srini/674/public/reuters/reut2-007.sgm',
          'http://web.cse.ohio-state.edu/~srini/674/public/reuters/reut2-008.sgm',
          'http://web.cse.ohio-state.edu/~srini/674/public/reuters/reut2-009.sgm',
          'http://web.cse.ohio-state.edu/~srini/674/public/reuters/reut2-010.sgm',
          'http://web.cse.ohio-state.edu/~srini/674/public/reuters/reut2-011.sgm',
          'http://web.cse.ohio-state.edu/~srini/674/public/reuters/reut2-012.sgm',
          'http://web.cse.ohio-state.edu/~srini/674/public/reuters/reut2-013.sgm',
          'http://web.cse.ohio-state.edu/~srini/674/public/reuters/reut2-014.sgm',
          'http://web.cse.ohio-state.edu/~srini/674/public/reuters/reut2-015.sgm',
          'http://web.cse.ohio-state.edu/~srini/674/public/reuters/reut2-016.sgm',
          'http://web.cse.ohio-state.edu/~srini/674/public/reuters/reut2-017.sgm',
          'http://web.cse.ohio-state.edu/~srini/674/public/reuters/reut2-018.sgm',
          'http://web.cse.ohio-state.edu/~srini/674/public/reuters/reut2-019.sgm',
          'http://web.cse.ohio-state.edu/~srini/674/public/reuters/reut2-020.sgm',
          'http://web.cse.ohio-state.edu/~srini/674/public/reuters/reut2-021.sgm']


stop=stopwords.words('english')


titles=[]
bodies=[]
topics=[]
places=[]
content=''
doc_list_of_set=[]
freq_dict={}
actual_uniq_words=[]
uni_dict={}
list_yes=[]
article_list=[]
ind_doc_uniq_words=[]
not_null_topics=[]
body_with_topic=[]
body_without_topic=[]
not_null_places=[]
null_places=[]

def removeStopWords(words,stop):                    #function to remove stop-words, numbers and special characters  
    
    temp_list=[]
    words=str(words).lower()
    words=re.sub("[^a-z]", ' ',words)               #regex to keep only words no number, no special characters 
    word_list=nltk.word_tokenize(words)             #tokenize the string, returns a list of words
    
    for word in word_list:
        word=word.lower()
        if word not in stop and len(word)>2:        #if word is not in the stop-word list and word > 2 characters then consider it   
            temp_list.append(word)
                    
    newWord=' '.join(temp_list)                     #build a new string and pass it back. Will be used for lemmatization
    return newWord

def threshold(size):
    max=int(raw_input("What is the maximum thresholding rate?"))
    min=int(raw_input("What is the minimum thresholding rate?"))
    up=max*size/100
    down=min*size/100
    
    for key in uni_dict.keys():
        if uni_dict[key]>down and uni_dict[key]<up :      #condition change >    and      < 
            list_yes.append(key)                         # take yes


def addToList(doc_list):
    
    for ele in doc_list:
        temp=[]
        for word in list_yes:
            if word in ele:
               temp.append(word)     
        actual_uniq_words.append(temp)            

def lemmatize(words):                               #function to lemmatize(stem) words
    stemmer=nltk.stem.porter.PorterStemmer()
    word_list=[]                                    
    for word in nltk.word_tokenize(words):                      #return a list of words. choose every word from that list 
        #word_list.append(WordNetLemmatizer().lemmatize(word,'v'))
        word_list.append(stemmer.stem(word))                                                  #lemmatize every word if possible  
    newWord=' '.join(word_list)                     # combine the word_list to give us a string. 
    return newWord                                  # return the string for further processing


def uniqueWordCounterInDoc(words):                  #function to find a set of unique words in a document(article) 
    dwords=nltk.word_tokenize(words)                #tokenize the string. returns a list of words 
    return frozenset(dwords)                        
                                                    #===========================
                                                    # convert the list into a frozenset(frozen set because it has a method hash() 
                                                    # which is required for further processing). Frozen set just means u promise you 
                                                    # won't change the contents of the set
                                                    #===========================
                                                                                                                                                 
def listIntegrator(setlist):                        #This function is used to integrate a list of sets 
    finalset=set()                                  #initial empty set
    for ind_set in setlist:                         #take each set in the list passed and union it with finalset
        finalset=finalset.union(ind_set)
    return finalset                                 
                                                    #===========================
                                                    # this will return the union of all distinct sets of each document and will take
                                                    # one master set of unique words across all documents             
                                                    #===========================

def createFreqDict(doc_sets,universal_set):         #function that is used to create freq counter for each unique word across all doc
                                                    #it takes the master set of unique words across all documents and list of sets of 
                                                    #unique words for each document 
    i=1
    for e in universal_set:                         #for every unique word in the master bedroom  
        for s in doc_sets:                          #for every set in the list of sets
            if e in s:                              #if the word from master list is in the current set then 
                if e in freq_dict.keys():           #if the word is already in the dictionary then 
                    freq_dict[e]+=1                 #increment its value(count) by 1
                else:                               #if word is not already a key in the dictionary 
                    freq_dict[e]=1                  #add the word as the key to the dictionary
        if i%100==0:            
            print "NO OF TERMS CHECKED: ",i         #status report, print after every 100 elements from the master set are processed.
        i=i+1                
    return freq_dict;                    


def changeList(doc_list):    
    x=[]
    for i in range(0,len(doc_list)):
        x.append(set(doc_list[i]))
    return x

def generateBinary(doc_list):
    binary_list=[]
    for ind_set in doc_list:
        temp=[0]*len(list_yes)
        for i in range(0,len(list_yes)):
            if list_yes[i] in ind_set:
                temp[i]=1
        binary_list.append(temp)
    return binary_list

def generateArticleDict(list_articles):
    list_dict=[]
    for article in list_articles:
        if article==None:
            list_dict.append({})
        else:    
            data=article.split()
            temp={}
            for word in list_yes:
                temp[word]=data.count(word)
            list_dict.append(temp)    
    return list_dict    


def main():                                         #this is the function where all the processing takes place    
    data=content.split("</REUTERS>")                #data is a list of all articles on one sgm file
    data=data[:len(data)-1]
    
    
    for article in data:
        bs=BeautifulSoup(article)                   

        titles.append(bs.find_all('title'))         #title contains titles of article of all sgm files
        
        p=re.compile('<TOPICS>(.*?)</TOPICS>') 
        topic_r=re.findall(p,article) 
        top_list=[]
        for topic in topic_r:
            p=re.compile('<D>(.*?)</D>')
            top_list=re.findall(p,topic)
            topics.append(top_list)

        temp=bs.find_all('body')                    #temp contains bodies of article of each sgm file
        
        v=None
        if len(temp)!=0 and top_list!=[]:
            v=removeStopWords(temp[0],stop) 
            v=lemmatize(v)
            body_with_topic.append(v)
            doc_list_of_set.append(uniqueWordCounterInDoc(v)) #set of unique words for each article added to list   
        elif len(temp)!=0 and top_list==[]:
            v=removeStopWords(temp[0].string,stop) 
            v=lemmatize(v)
            body_without_topic.append(v)
        elif len(temp)==0 and top_list!=[]:
            body_with_topic.append(v)
            doc_list_of_set.append(set()) #set of unique words for each article added to list
        else:
            v=temp    
            body_without_topic.append(v)
        bodies.append(v)         
            
        
        p=re.compile('<PLACES>(.*?)</PLACES>')
        places_r=re.findall(p,article)
    
        for place in places_r:
            p=re.compile('<D>(.*?)</D>')
            places.append(re.findall(p,place))
     

def topicAndBodyManipulator():
    for i in range(0,len(topics)):
        if(topics[i]==[]):
            null_places.append(places[i])
        else:
            not_null_topics.append(topics[i])        
            not_null_places.append(places[i])


def readyPrinter():
    temp=set(list_yes)
    for ind_set in doc_list_of_set:
        x=temp.intersection(ind_set)
        ind_doc_uniq_words.append(x)


def printer():
    
        
    file=open(r'/home/5/chandraj/Data Mining/fv1.txt','w')
    file1=open(r'/home/5/chandraj/Data Mining/fv2.txt','w')
    file2=open(r'/home/5/chandraj/Data Mining/fv3.txt','w')
    file2.write(str(term_freq_vector[0].keys()) + "\n")
    for i in range(0,len(body_with_topic)):
        file.write("DOC ID:"+str(i+1)+"\n")
        file.write("TOPICS:"+str(not_null_topics[i])+"\n")
        file.write("PLACES:"+str(not_null_places[i])+"\n")
        file.write("BINARY LIST OF WORDS:"+str(bin_feature_vector[i])+"\n")
        file.write("**********\n")
        file.write("\n")
        file1.write("DOC ID:"+str(i+1)+"\n")
        file1.write("TOPICS:"+str(not_null_topics[i])+"\n")
        file1.write("PLACES:"+str(not_null_places[i])+"\n")
        file1.write("LIST OF WORDS:"+str(ind_doc_uniq_words[i])+"\n")
        file1.write("**********\n")
        file1.write("\n")
        file2.write(str(term_freq_vector[i].values())+"\n")

for url in url_list:
    content=urllib.urlopen(url).read()
    print "CURRENT URL:",url
    main()
        
topicAndBodyManipulator()
universal_uniq_set=listIntegrator(doc_list_of_set)
uni_dict=createFreqDict(doc_list_of_set, universal_uniq_set) 
doc_list_of_set=changeList(doc_list_of_set)
threshold(len(doc_list_of_set))
addToList(doc_list_of_set)
readyPrinter()
bin_feature_vector=generateBinary(ind_doc_uniq_words)
term_freq_vector=generateArticleDict(body_with_topic)
printer()
print len(list_yes)
print len(term_freq_vector)
