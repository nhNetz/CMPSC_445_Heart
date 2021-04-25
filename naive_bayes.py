import pandas as pd
import math
from decimal import Decimal

X=pd.read_csv('heart_training.txt',sep=" ",header=None)
X.columns=['age','sex','cp','trtbps','chol','fbs','restecg','thalachh','exng','oldpeak','slp','caa','thall','output']
Xtest=pd.read_csv('heart_testing.txt',sep=" ",header=None)
Xtest.columns=['age','sex','cp','trtbps','chol','fbs','restecg','thalachh','exng','oldpeak','slp','caa','thall','output']

a=Xtest.shape[0] #number of rows in test data
b=X.shape[0] #number of rows in training data

j=0 #iterator for data function
def pdf(mean,std,xi):           #pdf for attribute
    return 1/math.sqrt(2*math.pi*pow(std,2))*math.exp(-pow((xi-mean),2)/2/pow(std,2))
def getresult():    
    tp = 0 #True Positive
    fp = 0 #False Positive
    tn = 0 #True Negative
    fn = 0 #False Negative
    type1Count=X[X.output==1].shape[0]
    typeN1Count=X[X.output==0].shape[0]
    Prob1=type1Count/X.shape[0]
    ProbN1=typeN1Count/X.shape[0]
    #print (X[X.type==1].shape[0]) #number of type 1
   # print (Prob1)
    X1=X[X['output'].isin([1])] #new df with type in 1
    avgAge=X1['age'].mean(axis=0) #avg for specific column
    avgTrtbps=X1['trtbps'].mean(axis=0)
    avgChol=X1['chol'].mean(axis=0)
    avgThalachh=X1['thalachh'].mean(axis=0)
    avgOldpeak=X1['oldpeak'].mean(axis=0)
    stdAge=X1['age'].std(axis=0)
    stdTrtbps=X1['trtbps'].std(axis=0)
    stdChol=X1['chol'].std(axis=0)
    stdThalachh=X1['thalachh'].std(axis=0)
    stdOldpeak=X1['oldpeak'].std(axis=0)
    XN1=X[X['output'].isin([0])] #new df with type in -1
    avgAgeN=XN1['age'].mean(axis=0) #avg for specific column
    avgTrtbpsN=XN1['trtbps'].mean(axis=0)
    avgCholN=XN1['chol'].mean(axis=0)
    avgThalachhN=XN1['thalachh'].mean(axis=0)
    avgOldpeakN=XN1['oldpeak'].mean(axis=0)
    stdAgeN=XN1['age'].std(axis=0)
    stdTrtbpsN=XN1['trtbps'].std(axis=0)
    stdCholN=XN1['chol'].std(axis=0)
    stdThalachhN=XN1['thalachh'].std(axis=0)
    stdOldpeakN=XN1['oldpeak'].std(axis=0)
    #for categorical data
    sex=0 #number of matching rows with type 1 and 0
    sexN=0
    cp=0 
    cpN=0
    fbs=0 
    fbsN=0
    restecg=0 
    restecgN=0 
    exng=0
    exngN=0
    slp=0
    slpN=0
    caa=0
    caaN=0
    thall=0
    thallN=0
    for j in range (0,a):
        for i in range(0,b):
            if X.at[i,'sex']==Xtest.at[j,'sex'] and X.at[i,'output']==1:
                sex+=1
            elif X.at[i,'sex']==Xtest.at[j,'sex']and X.at[i,'output']==0:
                sexN+=1
            else:
                continue
        for i in range(0,b):
            if X.at[i,'cp']==Xtest.at[j,'cp'] and X.at[i,'output']==1:
                cp+=1
            elif X.at[i,'cp']==Xtest.at[j,'cp']  and X.at[i,'output']==0:
                cpN+=1
            else:
                continue
        for i in range(0,b):
            if X.at[i,'fbs']==Xtest.at[j,'fbs'] and X.at[i,'output']==1:
                fbs+=1
            elif X.at[i,'fbs']==Xtest.at[j,'fbs']and X.at[i,'output']==0:
                fbsN+=1 
            else:
                continue
        for i in range(0,b):
            if X.at[i,'restecg']==Xtest.at[j,'restecg'] and X.at[i,'output']==1:
                restecg+=1
            elif X.at[i,'restecg']==Xtest.at[j,'restecg'] and X.at[i,'output']==0:
                restecgN+=1
            else:
                continue
        for i in range(0,b):
            if X.at[i,'exng']==Xtest.at[j,'exng'] and X.at[i,'output']==1:
                exng+=1
            elif X.at[i,'exng']==Xtest.at[j,'exng'] and X.at[i,'output']==0:
                exngN+=1
            else:
                continue
        for i in range(0,b):
            if X.at[i,'slp']==Xtest.at[j,'slp'] and X.at[i,'output']==1:
                slp+=1
            elif X.at[i,'slp']==Xtest.at[j,'slp'] and X.at[i,'output']==0:
                slpN+=1
            else:
                continue
        for i in range(0,b):
            if X.at[i,'caa']==Xtest.at[j,'caa'] and X.at[i,'output']==1:
                caa+=1
            elif X.at[i,'caa']==Xtest.at[j,'caa'] and X.at[i,'output']==0:
                caaN+=1
            else:
                continue
        for i in range(0,b):
            if X.at[i,'thall']==Xtest.at[j,'thall'] and X.at[i,'output']==1:
                thall+=1
            elif X.at[i,'thall']==Xtest.at[j,'thall'] and X.at[i,'output']==0:
                thallN+=1
            else:
                continue
                'age','sex','cp','trtbps','chol','fbs','restecg','thalachh','exng','oldpeak','slp','caa','thall','output'
        #for i in range (0,a):
        #multiplication of possibility of all continuous attributes
        Pis1C=pdf(avgAge,stdAge,Xtest.at[j,'age'])*pdf(avgTrtbps,stdTrtbps,Xtest.at[j,'trtbps'])*pdf(avgChol,stdChol,Xtest.at[j,'chol'])*pdf(avgThalachh,stdThalachh,Xtest.at[j,'thalachh'])*pdf(avgOldpeak,stdOldpeak,Xtest.at[j,'oldpeak'])
        PisN1C=pdf(avgAgeN,stdAgeN,Xtest.at[j,'age'])*pdf(avgTrtbpsN,stdTrtbpsN,Xtest.at[j,'trtbps'])*pdf(avgCholN,stdCholN,Xtest.at[j,'chol'])*pdf(avgThalachhN,stdThalachhN,Xtest.at[j,'thalachh'])*pdf(avgOldpeakN,stdOldpeakN,Xtest.at[j,'oldpeak'])
        #print(i,Pis1C,PisN1C)
        #possibility of 1 and 0
        Pis1=Pis1C*sex/type1Count*cp/type1Count*fbs/type1Count*restecg/type1Count*exng/type1Count*slp/type1Count*caa/type1Count*thall/type1Count*Prob1
        PisN1=PisN1C*sexN/typeN1Count*cpN/typeN1Count*fbsN/typeN1Count*restecgN/typeN1Count*exngN/typeN1Count*slpN/typeN1Count*caaN/typeN1Count*thallN/typeN1Count*ProbN1
        if Pis1>PisN1:
            if Xtest.at[j,'output']==1:
                tp+=1
            else:
                fp+=1
            print(j,'is 1','P of being 1','%.2E'% Decimal(Pis1),'P of being -1','%.2E'% Decimal(PisN1) )
        else:
            if Xtest.at[j,'output']==0:
                    tn+=1
            else:
                fn+=1
            print(j,'is -1','P of being 1','%.2E'% Decimal(Pis1),'P of being -1','%.2E'% Decimal(PisN1))
        #print('type1',type1Count,sl,sw,pl,pw,slN,swN,plN,pwN)
        sex=0 #number of matching rows with type 1 and 0
        sexN=0
        cp=0 
        cpN=0
        fbs=0 
        fbsN=0
        restecg=0 
        restecgN=0 
        exng=0
        exngN=0
        slp=0
        slpN=0
        caa=0
        caaN=0
        thall=0
        thallN=0   
    print('tp:',tp,'fp:',fp,'tn:',tn,'fn:',fn,'accuracy:', (tp+tn)/a)
getresult()    