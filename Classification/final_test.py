'''
Created on Oct 9, 2014

@author: GAURAV
'''
'''
Created on Oct 8, 2014

@author: GAURAV
'''
outputFile4=open(r"data.tab","w+")
outputFile5=open(r"data5.tab","w+")
outputFile6=open(r"data6.tab","w+")
outputFile7=open(r"data7.tab","w+")
outputFile8=open(r"data8.tab","w+")

path1=r'fv2.txt'
file1=open(path1,'r')                        
uniq_topics=set()
content1=file1.read()
data1=content1.split("**********\n")
data1=data1[:-1]

path=r'fv3.txt'
file=open(path,'r')
content=file.read()
data=content.split("\n")
data=data[:-1]
uniq_words=eval(data[0])
words_u=[]
for word in uniq_words:
    words_u.append(str(word))
data=data[1:]
lod_words=[]
uni_topics={}
feature_vector=[]
row_data=[]


for i in range(0,len(data1)):
    article=data1[i]
    lines=article.split("\n")
    if(i==0):
        topics=lines[1].split(":")
    else:
        topics=lines[2].split(":")
    topics=eval(topics[1])
    for topic in topics:
        if uni_topics.has_key(topic):
            uni_topics[topic]+=1
        else:
            uni_topics[topic]=1        

for j in range(0,len(data)):
    article=eval(data[j])
    word_dict={}
    for k in range(0,len(article)):
        if article[k]>0:
            word_dict[str(uniq_words[k])]=article[k]
    #print word_dict        
    lod_words.append(word_dict)

#d_t=["d" for i in range(0,len(words_u))]
d_t=[]


indices=[]
for i in range(0,len(words_u)):
    article=eval(data[i])
    if uni_topics.has_key(words_u[i])==False:
        row_data.append(words_u[i])
        d_t.append("d")
    else:
        indices.append(i)
         

for i in range(0,len(data)):
    article=eval(data[i])
    temp=[]
    for j in range(0,len(article)):
        if j not in indices:
            temp.append(str(article[j]))
    feature_vector.append(temp)        
        
t=["" for i in range(0,len(d_t))]

outputFile4.write("DocID" + "\t" + "Topic" + "\t" +"Places"+"\t"+"\t".join(row_data) + "\n")
outputFile4.write("d" + "\t" + "d" + "\t" +"d"+"\t"+"\t".join(d_t)+ "\n")
outputFile4.write("meta" + "\t" + "class" + "\t"+" "+"\t".join(t)+ "\n")

outputFile5.write("DocID" + "\t" + "Topic" + "\t" +"Places"+"\t"+"\t".join(row_data) + "\n")
outputFile5.write("d" + "\t" + "d" + "\t" +"d"+"\t"+"\t".join(d_t)+ "\n")
outputFile5.write("meta" + "\t" + "class" + "\t"+" "+"\t".join(t)+ "\n")

outputFile6.write("DocID" + "\t" + "Topic" + "\t" +"Places"+"\t"+"\t".join(row_data) + "\n")
outputFile6.write("d" + "\t" + "d" + "\t" +"d"+"\t"+"\t".join(d_t)+ "\n")
outputFile6.write("meta" + "\t" + "class" + "\t"+" "+"\t".join(t)+ "\n")

outputFile7.write("DocID" + "\t" + "Topic" + "\t" +"Places"+"\t"+"\t".join(row_data) + "\n")
outputFile7.write("d" + "\t" + "d" + "\t" +"d"+"\t"+"\t".join(d_t)+ "\n")
outputFile7.write("meta" + "\t" + "class" + "\t"+" "+"\t".join(t)+ "\n")

outputFile8.write("DocID" + "\t" + "Topic" + "\t" +"Places"+"\t"+"\t".join(row_data) + "\n")
outputFile8.write("d" + "\t" + "d" + "\t" +"d"+"\t"+"\t".join(d_t)+ "\n")
outputFile8.write("meta" + "\t" + "class" + "\t"+" "+"\t".join(t)+ "\n")

x=int(0.8*len(data))
y=int(0.6*len(data))
for i in range(0,len(data1)):
    article=data1[i]
    words=data[i]
    lines=article.split("\n")
    topics=[]
    places=[]
    docid=-1
    if(i==0):
        places=lines[2].split(":")
        topics=lines[1].split(":")
        docid=lines[0].split(":")
    else:
        places=lines[3].split(":")    
        topics=lines[2].split(":")
        docid=lines[1].split(":")
    places=eval(places[1])    
    topics=eval(topics[1])
    docid=docid[1]
    max=0
    max_topic=topics[0]
    for topic in topics:
        if uni_topics[topic]>max:
            max=uni_topics[topic]
            max_topic=topic 
    words=eval(words)
    w=[]
    outputFile4.write(docid+"\t"+max_topic+"\t"+" ".join(places)+"\t" +"\t".join(feature_vector[i]))
    outputFile4.write("\n")
    
    if(i<x): 
        outputFile5.write(docid+"\t"+max_topic+"\t"+" ".join(places)+"\t" +"\t".join(feature_vector[i]))
        outputFile5.write("\n")
    if(i>=x and i<len(data)):
        outputFile6.write(docid+"\t"+max_topic+"\t"+" ".join(places)+"\t" +"\t".join(feature_vector[i]))
        outputFile6.write("\n")
    if(i<y): 
        outputFile7.write(docid+"\t"+max_topic+"\t"+" ".join(places)+"\t" +"\t".join(feature_vector[i]))
        outputFile7.write("\n")
    if(i>=y and i<len(data)):
        outputFile8.write(docid+"\t"+max_topic+"\t"+" ".join(places)+"\t" +"\t".join(feature_vector[i]))        
        outputFile8.write("\n")
        