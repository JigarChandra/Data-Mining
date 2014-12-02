'''
Created on Nov 18, 2014

@author: GAURAV
'''
'''
Created on Nov 14, 2014

@author: GAURAV
'''

import random as ran
from numpy import *
import numpy
import timeit

time1 = -timeit.default_timer()

path=r'fv3.txt'
file=open(path,'r')
content=file.read()
data=content.split("\n")
data=data[:-1]
uniq_words=eval(data[0])
data=data[1:]

num_dim=len(eval(data[0]))
print "Number of dimensions:",num_dim
k=raw_input("enter the k value? choose from 16,32,64 and 128")
k=int(k)
hash_dict={}



a_list=ran.sample(range(num_dim),k)
b_list=ran.sample(range(num_dim),k)

for i in range(0,k):
    a=a_list[i]
    b=b_list[i]
    hash_list=[]
    for x in range(0,num_dim):
        h=(a*x+b)%num_dim
        hash_list.append(h)
    hash_dict[i]=hash_list
final_hash_list=ones((k,len(data)),dtype=int16)
#convert into array of -1

for row in range(0,k):
    for column in range(0,len(data)):
        final_hash_list[row][column]*=-1

temp=[]
for i in range(0,len(data)):
    t_row=eval(data[i])
    temp.append(t_row)

data=numpy.array(temp)
temp=[]
data=numpy.transpose(data)

                
for row in range(0,len(data)):
    print "row number=",row
    for row_f in range(0,k):
        for column in range(0,len(data[0])):
            if(data[row][column]!=0):
                x1=final_hash_list[row_f][column]
                y1=hash_dict[row_f][row]
                if(x1==-1):
                    final_hash_list[row_f][column]=y1
                elif(x1>y1):
                    final_hash_list[row_f][column]=y1    

numpy.savetxt("Matrix"+str(k)+".txt",final_hash_list)
time1 += timeit.default_timer()
print "Time for lshasher:",str(time1)

        
        
    
