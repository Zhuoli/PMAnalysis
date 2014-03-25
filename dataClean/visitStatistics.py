'''
Created on Mar 20, 2014

@author: CT61557
'''
import pandas as pd
from EmailCommunication.EmailAnimation import  *

def reverseDate(day):
    days=day.split('-')
    year=days[0]
    month=str((int)(days[1]))
    day=str((int)(days[2]))
    return month+'/'+day+'/'+year
# get the PR visit history table saved in this project folder
def getVisitStatistics(path,project,name='',flag=False,saveName='visitHistory.csv'):
    df=pd.read_csv(path)
    df.index=df.Date
    df=df.drop(['Unnamed: 0','Date'], axis=1)
    start='2013-04-11 00:00:01'
    dicts={}
    for i in range(0,365):
        start=addEndDate(start,1)
        date=start.split(' ')[0]
        if '-' in df.index[0]:
            dicts[date]=0
        else:
            dicts[reverseDate(date)]=0;
    indexs = set(df.index)
    #print 'dicts.keys: ',dicts.keys()
    #print 'indexs: ',indexs
    dataFrameType = type(df)
    for index in indexs:
        #if not index in dicts.keys():
        #    continue
        frame = df.ix[index]
        if type(frame) == dataFrameType:
            if name != '':
                ls = frame['Name'].map(lambda x : name in x)
                #print ls
                frame=frame[ls]
            dicts[index.strip()]=len(frame['Name'])
        else:
            if name in frame['Name']:
                dicts[index]=1
            else:
                dicts[index]=0
    date=[]
    count=[]
    for key in dicts.keys():
        date.append(key)
        count.append(dicts[key])
    dicts={'Date':date,'Count':count}
    out=pd.DataFrame(dicts)
    out=out[['Date','Count']]
    out.to_csv('../../result/'+project+'/' + saveName)

def clean2Statistics(fromPath,toPath,column='Source'):
    df=pd.read_csv(fromPath)
    data=df[['Date Start',column]]
    data.columns=['Date','Name']
    ls=data.Name=='Robert'
    data = data[ls]
    data.Date=data.Date.map(lambda x : x.split(' ')[0])
    data.to_csv(toPath)
    return 

#project='KnowledgeEcoSystem2'
#fromPath='../../data/gephidata.csv'
#destPath='../../result/'+project+'/emailHistory.csv'
#clean2Statistics(fromPath,destPath)
#getVisitStatistics('../../result/'+project+'/emailHistory.csv',project,flag=False,name='Robert',saveName='emailHistory.csv')

######## Project Repository visit rate ##############
project = 'KnowledgeEcoSystem2'
members =getMembersName(project,path='../../result/' + project +'/TeamMembers.txt')
print members
path='../../result/'+project+'/PRResult.csv'
#getVisitStatistics(path,project,name='Robert')