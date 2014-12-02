'''
Created on Oct 8, 2014

@author: GAURAV
'''
import site
import time

import Orange
from Orange.evaluation import scoring
import orngStat, orngTest


learners=[Orange.classification.bayes.NaiveLearner(name="bayes")]

data=Orange.data.Table("data.tab")
data5=Orange.data.Table("data5.tab")
data7=Orange.data.Table("data7.tab")
#x=raw_input("what is the proportion of test an train data? eg: 0.6,0.7 etc")
print "FOR THE 80-20 SPLIT:"

s_time=time.time()
res=Orange.evaluation.testing.proportion_test([learners[0]], data, 0.8,stratification=True,times=1,store_classifiers=True)
e_time=time.time()

cm=Orange.evaluation.scoring.confusion_matrices(res,class_index=0)

start_time=time.time()
bayes=learners[0](data5)
end_time=time.time()


rows = [str(learners[0].name), str(orngStat.CA(cm)[0]), str(scoring.Precision(cm)[0]), str(scoring.recall(cm)[0]), str(scoring.F1(cm)[0])]
headers=["Classifier","CA","Precision","Recall","F1-score"]
print("\t  ".join(headers))
print("\t".join(rows))

print"Offline time:"+str(end_time-start_time)
print"Online time:"+str(e_time-s_time-(end_time-start_time))
print("\n\n")

    
print"FOR THE 60-40 SPLIT:"
s_time=time.time()
res=Orange.evaluation.testing.proportion_test(learners, data, 0.6,stratification=True,times=1,store_classifiers=True)
e_time=time.time()
cm=Orange.evaluation.scoring.confusion_matrices(res,class_index=0)

start_time=time.time()
bayes=learners[0](data7)
end_time=time.time()

rows = [str(learners[0].name), str(orngStat.CA(cm)[0]), str(scoring.Precision(cm)[0]), str(scoring.recall(cm)[0]), str(scoring.F1(cm)[0])]
headers=["Classifier","CA","Precision","Recall","F1-score"]
print("\t  ".join(headers))
print("\t".join(rows))
print"Offline time:"+str(end_time-start_time)
print"Online time:"+str(e_time-s_time-(end_time-start_time))

