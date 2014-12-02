'''
Created on Oct 4, 2014

@author: Jigar
'''
import csv
import sys
from MyKNN import KNN

def parseDM(filepath = r'fv3.csv'):
    dataMatrix = []

    matrix = []
    word_list = []
    topic_list = []
    with open(filepath, 'rb') as csv_file:
        reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        for row in reader:
            dataMatrix.append(row)
    
    for item in dataMatrix[0]:       
        if "_" not in item:
            word_list.append(item)
        elif "t_" in item:             
            topic_list.append(item[2:])        
    word_list = word_list[1:] # Remove 'Article #'
    words_topics_size = len(topic_list) + len(word_list)

    for row in dataMatrix[1:]:
        matrix.append( [row[0]] + map(int, row[1:1 + words_topics_size]) )
    return {"topic_list":topic_list, "word_list": word_list, "matrix": matrix}


##### MAIN #####
dataMatrix = parseDM()
temp_topic = []
nullbodycount = 0
wlist = len(dataMatrix["word_list"])
printfirstten=0
for topic in dataMatrix["matrix"]:
    temp_topic = topic[wlist+1:]
    if temp_topic.count(0) == len(temp_topic):
        dataMatrix["matrix"].remove(topic) 
arg_list = sys.argv
if len(arg_list) != 5:
    print "Calling syntax: python RunningKNN_KNN.py -k <NumberofNeighbors> -t <SplitPercentage>"
    sys.exit(1)

if arg_list[1] == '-k':
    k = int(arg_list[2])
elif arg_list[1] == '-t':
    t = int(arg_list[2])

if arg_list[3] == '-k':
    k = int(arg_list[4])
elif arg_list[3] == '-t':
    t = float(arg_list[4])


knn = KNN(dataMatrix, k)
knn.split_Data(t)
