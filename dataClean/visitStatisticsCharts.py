'''
Created on Mar 27, 2014

@author: CT61557
'''
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt


project = 'KnowledgeEcoSystem2'

def drawVisitHistory(project):
    prPath = '../../result/'+ project +'/PRvisitHistory.csv'
    kpPath = '../../result/'+ project +'/KPvisitHistory.csv'
    saveDir='../../result/' + project +'/charts/'
    try:
        pr=pd.read_csv(prPath,index_col=0)
        kp=pd.read_csv(kpPath,index_col=0)
    except:
        sys.stderr.write('IOError: lack input file')
        sys.exit(0)
    prMmebers = set(pr.columns.values)
    kpMembers = set(kp.columns.values)    
    members=list(prMmebers.intersection(kpMembers))

    for member in members:
        dicts={}
        dicts['kpVisit']=kp[member].values
        dicts['prVisit']=pr[member].values
        df=pd.DataFrame(dicts,index=pr.index)
        figure=plt.Figure();
        df.plot(subplots=True,kind='line',ylim=0,figsize=(15,7),title=member+'\'s visit History')
        plt.savefig(saveDir+member+'.png')
        df.to_csv(saveDir+'tables/'+member +'.csv')
        plt.close()
  
 
for project in os.listdir('../../result'):
    print 'Drawing PROJECT : ' + project
    path = '../../result/'+project+'/charts' 
    if not os.path.isdir(path):
        os.mkdir(path);
        os.mkdir(path+'/tables')
    drawVisitHistory(project) 