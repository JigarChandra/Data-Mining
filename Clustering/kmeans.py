'''
Created on Oct 24, 2014

@author: Jigar
'''
from __future__ import division
from Orange import data
from Orange import clustering
from Orange import distance
import math
import random
import sys
import timeit
random.seed(100)
data = data.Table("data.tab")  
arg_list = sys.argv
if arg_list[1] =='0':
    time = -timeit.default_timer()
    km = clustering.kmeans.Clustering(data, ((int)(arg_list[2])), minscorechange=0, distance=distance.Euclidean)
    time += timeit.default_timer()
    print "Time to cluster = " + str(time)
elif arg_list[1] == '1':
    time1 = -timeit.default_timer()
    km = clustering.kmeans.Clustering(data, ((int)(arg_list[2])), minscorechange=0, distance=distance.Manhattan)
    time1 += timeit.default_timer()
    print "Time to cluster = " + str(time1)        
count = [0]*((int)(arg_list[2]))

for item in km.clusters:
    count[item]+=1
i= 0
# for counts in count:
#     print i," ",counts
#     i+=1              
labels = []    
l_l=[]
for i in range (0,((int)(arg_list[2]))):
    l_l.append([])
    labels.append({})
#===============================================================================
# for item,instance in km.clusters,data:
#     if item==0:
#         if instance not in labels.keys():
#             labels[instance] = item
#         else:
#             labels[instance] +=1
#===============================================================================
# print labels 
for i in range(0,((int)(arg_list[2]))):
    for j in range(0,len(km.clusters)):
        if km.clusters[j]==i:
            l_l[i].append(j)            
list_of_labels = []
outer_list = []
for i in range (0,((int)(arg_list[2]))):
    list_of_labels.append([])
ctr =-1    
for l in l_l:
    ctr+=1
    for i in l:
        list_of_labels[ctr].append(str(data[i][-1]))
        outer_list.append(str(data[i][-1]))
unique_labels = set(outer_list) 
for element in unique_labels:
    ctr = -1 
    for listt in list_of_labels:
        count1=0
        ctr+=1
        for aelement in listt:
            if element==aelement:
                count1+=1;
        labels[ctr][element]=count1
entropy_list =[]
ctr = -1 
for label in labels:
    ctr+=1
    entropy = 0.0
    for i in label.values():
        if i != 0:  
            entropy+=(i/count[ctr])*(math.log((count[ctr]/i),2)) 
    entropy_list.append(entropy)              
total_instances = len(outer_list)
parent_entropy = 0.0
label_ctr =0
for entropy in entropy_list:
    parent_entropy+=(sum(labels[label_ctr].values())/total_instances)*entropy 
    label_ctr+=1 
print "Entropy",parent_entropy 
meann = float(sum(count)/len(count))
std_dev = 0.0
for counts in count:
    std_dev+=(counts-meann)*(counts-meann)
std_dev = std_dev/len(count)    
std_dev = math.sqrt(std_dev)
print 'std_dev is ', std_dev    
                                           