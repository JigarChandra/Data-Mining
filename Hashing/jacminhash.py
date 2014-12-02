'''
Created on Nov 16, 2014

@author: Jigar
'''
from __future__ import division
import numpy
import timeit
import sys
arg_list = sys.argv
def hash_to_jaccard(hash_number):
    data = numpy.loadtxt("Matrix"+str(hash_number)+".txt")
    fv = numpy.transpose(data)  
    jac = numpy.ones((len(fv), len(fv)))
    for i in range(0,len(fv)-1):
        if i%200==0:
            print "loading for",i
        for j in range(i,len(fv)):
            f11=0
            for k in range(0,len(fv[0])):
                if fv[i][k]==fv[j][k]:
                    f11+=1
            jacc=0.0
            jacc = f11/len(fv[0])             
            jac[i][j]=jacc
    return jac
time = -timeit.default_timer()         
jaccardMin = hash_to_jaccard(int(arg_list[1]))    
jac = numpy.loadtxt("NumpyJaccard.txt")
MSE = 0.0
for i in range(0,len(jac)):
    if i%1000==0:
            print "computing for",i
    for j in range(i+1,len(jac)):
        MSE+=((jaccardMin[i][j]-jac[i][j])*(jaccardMin[i][j]-jac[i][j]))
denom = (len(jac)*(len(jac)-1))/2          
MSE = MSE/denom   
time+= timeit.default_timer()
print "MSE",MSE
print  "Time to compute",str(time) 