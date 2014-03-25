'''
Created on Mar 18, 2014

@author: CT61557
'''

from EmailCommunication.EmailCommunicationDraw import cleanData
import pandas as pd
from FilePaths import *

def strip(s):
    return s.strip()
def lastName(name):
    if ',' in name:
        return name.split(',')[1].strip()
    else:
        return name
def mapHelper(cc,TeamMembers):
    if cc in TeamMembers:
        return lastName(cc)
    else:
        return 'OutTarget'
def filterName(s,TeamMembers):
    if ';' in s:
        strs=s.split(';')
        strs=map(strip,strs)
        CCS=map(lambda foo : mapHelper(foo,TeamMembers),strs)
        users=''
        for cc in CCS:
            users = users+cc +','
        users.strip(',')
        return users
    else:
        return str
def getMembersName(projectName,path=None):
    if path==None:
        path ='../result/'+ projectName +'/Teammembers.txt'
    f = open(path)
    names= f.readlines()
    members=[]
    #print names
    for name in names:
        name = name.strip('\r\n')
        name=name.strip()
        if len(name) ==0:
            continue
        members.append(name)
    return members
def addEndDate(time,interval,seperator='-'):
    bigMonths=[1,3,5,7,8,10,12]
    flag=0
    space=''
    if ' ' in time:
        times=time.split(' ')
        day=times[0]
        clock=times[1]
        space=' '
    else:
        day=time
        clock=''
    days=day.split(seperator)
    year=int(days[0])
    month=int(days[1])
    day=int(days[2])
    day=day+interval
    if day==29 and year%4!=0 and month==2:
        day=1
        flag=1
    elif day==30 and month==2:
        day=1
        flag=1
    elif day==31 and month not in bigMonths:
        day=1
        flag=1
    elif day==32:
        day=1
        flag=1
    month = month+flag;
    if month>12:
        month=1
        year=year+1
    if month<10:
        month = '0'+str(month)
    else:
        month=str(month)
    if day<10:
        day='0' + str(day)
    else:
        day=str(day)
    return str(year) +seperator+month + seperator +day +space + clock
    
def splitData(cleand):
    dates=[]
    sources=[]
    targets=[]
    labels=[]
    for i in range(0,len(cleand.Target)):
        row = cleand.ix[i]
        target = row['Target']
        if ',' in target:
            date = row['Date Start']
            source=row['Source']
            label = row['Normalized Subject']
            names = target.split(',')
            for name in names:
                name = name.strip()
                if len(name) != 0:
                    dates.append(date)
                    sources.append(source)
                    targets.append(name)
                    labels.append(label)
        else:
            dates.append(row['Date Start'])
            sources.append(row['Source'])
            targets.append(row['Target'])
            labels.append(row['Normalized Subject'])
    dicts={'Date Start':dates,'Source':sources,'Target':targets,'Label':labels}
    df=pd.DataFrame(dicts,columns=['Date Start','Source','Target','Label'],index=range(0,len(dates)))
    df['Date End']=df['Date Start'].map(lambda x :addEndDate(x,1))
    return df
            
def clean4gephi(projectName):
    members = getMembersName(projectName)
    senders,cleand = cleanData(cleaned_data,TeamMembers=members)
    cleand = cleand.ix[1:]
    cleand.Source=cleand.Source.map(lambda foo : mapHelper(foo,members))
    cleand.Target=cleand.Target.map(lambda foo : filterName(foo,members))
    data = splitData(cleand)
    #data=cleand
    #data['ID'] = data.Source  + data.Target 
    data.index = range(0,len(data.Target))
    #data.columns=['Date Start','Date End','Source','Target','Label']
    data.to_csv(gephiData)
