from __future__ import division
import math
import sys
from Orange import data, distance, clustering


iris = data.Table("data1.tab")
arg_list = sys.argv
#matrix = misc.SymMatrix(len(iris))
if arg_list[1] =='0':
	matrix = distance.distance_matrix(iris, distance.Euclidean)
elif arg_list[1] =='1':
	matrix = distance.distance_matrix(iris, distance.Manhattan)
clustering1 = clustering.hierarchical.HierarchicalClustering()
clustering1.linkage = clustering.hierarchical.SINGLE
root = clustering1(matrix)

root.mapping.objects = iris





#===============================================================================
# def dictCreator(node,index):
#     if node.left!=None:
#         temp=node.left
#         list_doc=[]
#         for point in temp:
#             docid=str(point["DocID"])
#             docid=int(docid)
#             list_doc.append(docid)
#         dict_topics[index]=list_doc
#         print dict_topics.keys()
#         index+=1
#         dictCreator(temp,index)
#     if node.right!=None:
#         temp=node.right
#         list_doc=[]
#         for point in temp:
#             docid=str(point["DocID"])
#             docid=int(docid)
#             list_doc.append(docid)
#         dict_topics[index]=list_doc
#         index+=1
#         print dict_topics.keys()
#         dictCreator(temp,index)
#         #dict_topics[index]=list_doc
#===============================================================================
       
    
count = 1
clusterIndex = 0
dict_topics = {}
dict_clusterMapping = {}
list_dictionaries = []
def list_of_nodes(node, l_nodes):
    global clusterIndex, dict_topics, dict_clusterMapping, list_dictionaries
    
    left_node = node.left
    right_node = node.right
    l_nodes.append(left_node)
    l_nodes.append(right_node)
    for i in range(0, int(arg_list[2])):
        for cluster in l_nodes:
            temp_list = []
            topic_dict = {}
            for point in cluster:
                docid = str(point["DocID"])
                docid = int(docid)
                topic = str(iris[docid - 1]["Topic"])
                if topic in topic_dict.keys():
                    c = topic_dict[topic]
                    c += 1
                    topic_dict[topic] = c
                else:
                    topic_dict[topic] = 1    
                    temp_list.append(docid)     
                    dict_clusterMapping[docid] = clusterIndex
            dict_topics[clusterIndex] = temp_list
            list_dictionaries.append(topic_dict)
            clusterIndex += 1
        #entropyCalculator(list_dictionaries)    
        
        list_dictionaries=[]  
        #l_nodes=[]
        splitclusters = []
        height = -1
        for clusters in l_nodes:
            if clusters.height > height:
                splitclusters=[clusters]
                height = clusters.height
            elif clusters.height == height:
                splitclusters.append(clusters)
        for clusters in splitclusters:
            l_nodes.remove(clusters)
            l_nodes.append(clusters.left)
            l_nodes.append(clusters.right)
#===============================================================================
# for point in listClusters:
#     temp=listClusters
#     docid=str(point["DocID"])
#     docid=int(docid)     
#     print str(docid),type(docid)
#===============================================================================
index=0

node_list=[]
#node_list.append(root)
list_of_nodes(root,node_list)
#print len(l_l) 



labels=[]
temp_dict_keys=dict_clusterMapping.keys()
for i in range(0,len(dict_clusterMapping.keys())):
    #print str(temp_dict_keys[i])+":"+str(dict_clusterMapping[temp_dict_keys[i]])
    labels.append(dict_clusterMapping[temp_dict_keys[i]])
#print str(dict_clusterMapping[1])




#===============================================================================
# for element in dict_topics.keys():
#     print dict_topics[element]
#===============================================================================
n_clusters_=len(dict_topics.keys())
data2 = data.Table("data.tab")
count = [0]*(n_clusters_)
labels1 = []
l_l=[]
for i in range (0,n_clusters_):
    l_l.append([])
    labels1.append({})
for item in labels:
    count[int(item)]+=1
for i in range(0,n_clusters_):
    for j in range(0,len(labels)):
        if labels[j]==i:
            l_l[i].append(j)            
list_of_labels = []
outer_list = []
for i in range (0,n_clusters_):
    list_of_labels.append([])
ctr =-1    
for l in l_l:
    ctr+=1
    for i in l:
        list_of_labels[ctr].append(str(data2[i][-1]))
        outer_list.append(str(data2[i][-1]))        
unique_labels = set(outer_list) 
for element in unique_labels:
    ctr = -1 
    for listt in list_of_labels:
        count1=0
        ctr+=1
        for aelement in listt:
            if element==aelement:
                count1+=1;
        labels1[ctr][element]=count1
entropy_list =[]
ctr = -1 
for label in labels1:
    ctr+=1
    entropy = 0.0
    for i in label.values():
        if i != 0 and (i/count[ctr]!=1): 
#             print (float(i)/float(count[ctr]),float((math.log((count[ctr]/i),2)))),float((float(i)/float(count[ctr]))*float((math.log((count[ctr]/i),2))))
            entropy+=float((float(i)/float(count[ctr]))*float((math.log((count[ctr]/i),2)))) 
    entropy_list.append(entropy) 
#print entropy_list                     
total_instances = len(outer_list)
parent_entropy = 0.0
label_ctr =0
for entropy in entropy_list:
    parent_entropy+=float(float(sum(labels1[label_ctr].values()))/float(total_instances))*entropy 
    label_ctr+=1 
print "Entropy",parent_entropy
print 'number of clusters', n_clusters_ 
sum = 0.0
for keys in dict_topics.keys():
    temp = len(dict_topics[keys])
    sum += temp
meann = sum/len(dict_topics.keys())
std_dev=0.0
for keys in dict_topics.keys():
    temp = len(dict_topics[keys])
    std_dev+=(temp-meann)*(temp-meann)
std_dev = std_dev/len(dict_topics.keys())    
std_dev = math.sqrt(std_dev)
print 'std_dev is ', std_dev  