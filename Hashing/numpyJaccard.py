'''
Created on Nov 16, 2014

@author: Jigar
'''

from __future__ import division
import numpy
import timeit
time = -timeit.default_timer()
path=r'fv3.txt'
file1=open(path,'r')
content=file1.read()
data=content.split("\n")
data=data[:-1]
data=data[1:]
fv = []
for datas in data:
    arr =eval(datas)
    for i in range(0,len(arr)):
        if arr[i]>1:
            arr[i]=1
    fv.append(numpy.array(arr))
# outputFile1=open(r"NumpyJaccardMatrix.txt","w+")
jac = numpy.ones((len(fv), len(fv)))
# jaccard = []
# for i in range(0,len(fv)):
#     jaccard.append([])
for i in range(0,len(fv)-1):
    for j in range(i,len(fv)):
        f11=numpy.dot(fv[i],fv[j])
        f=numpy.dot(fv[i],fv[i])+numpy.dot(fv[j],fv[j])-numpy.dot(fv[i],fv[j])
        jacc=0.0
        jacc = f11/f             
        jac[i][j]=jacc      
numpy.savetxt("NumpyJaccard.txt",jac) 
time+=timeit.default_timer()
print "Time to compute",time     
#         outputFile1.write(str(jacc))
#         outputFile1.write('\n')

