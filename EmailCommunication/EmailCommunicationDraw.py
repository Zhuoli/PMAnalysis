'''
@author: zhuoli
'''
'''
Created on Mar 12, 2014

@author: CT61557
'''
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import os
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
        return cc
    else:
        return 'OutTarget'
def filterName(s,TeamMembers):
    if ';' in s:
        strs=s.split(';')
        strs=map(strip,strs)
        CCS=map(lambda foo : mapHelper(foo,TeamMembers),strs)
        users=''
        for cc in CCS:
            users = users+cc +';'
        users.strip(',')
        return users
    else:
        return str
def cleanData(cleaned_data,filter=False,TeamMembers=[]):
    print 'emailPath:  ' + emailPath
    if os.path.isfile(cleaned_data):
        print 'cleand data'
        cleand = pd.read_csv(cleaned_data, names =['Date Start','Source','Target','Normalized Subject'])
        cleand.index=cleand.Source
        senders = set(cleand.index)
        return senders,cleand
    else:
        if emailPath== '../data/EmailR_Robert.xls':
            email =pd.read_excel(emailPath,'2003_Deleted_Items')
            print email.columns
            cleand = email[[u'Received',u'Created',u'Modified',u'From', u'CC', u'To',u'Normalized Subject']]
            cleand['Receiver']=cleand.CC +';' + cleand.To
            cleand=cleand.drop(['CC','To'], axis=1)
            cleand=cleand[['Received','From','Receiver','Normalized Subject']]
        else:
            email =pd.read_excel(emailPath,'Sent_Items')
            print email.columns
            cleand = email[[u'Sent',u'Created',u'Modified',u'Sender Name', u'CC', u'To',u'Normalized Subject']]
            cleand['Receiver']=cleand.CC +';' + cleand.To
            cleand=cleand.drop(['CC','To'], axis=1)
            cleand=cleand[['Sent','Sender Name','Receiver','Normalized Subject']] 
    cleand.columns=['Date Start','Source','Target','Normalized Subject']
    cleand=cleand.dropna()
    if filter:
        if len(TeamMembers)==0:
            print "To filter data, pls give team members"
            return
        ls=cleand.Source.map(lambda x : x in TeamMembers)
        cleand=cleand[ls] 
        cleand.Source=cleand.Source.map(lambda x : lastName(x))
        cleand.Target = cleand.Target.map(lambda x : filterName(x,TeamMembers))
    #print 'Cleand columns: ',cleand.columns
    cleand.to_csv(cleaned_data,encoding='utf-8')
    cleand.index=cleand.Source
    senders = set(cleand.index)
    return senders,cleand
#print senders

def getMembersName(projectName):
    f = open('../result/'+ projectName+'/Teammembers.txt')
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

def getProjectS2R(senders,members,cleand):   
    S2R={}
    #print 'Cleand.index: ',cleand.index
    #print 'members: ',members
    for sender in senders:
        S2R[sender] = set()
    for sender in senders:
        if sender not in members:
            continue
        if sender not in cleand.index:
            print 'sender ' + sender + ' not in cleand.index'
            continue
        #print 'Sender: ' + sender +' surived'
        table = cleand.ix[sender] 
        for cc in table['Target']:
            for u in cc.split(';'):
                u=u.strip()
                if u in members:
                    S2R[sender].add(u)   
    #print 'TeamMembers: ', members
    #print 'S2R senders: ',S2R.keys()
    EcoS2R={}
    for member in members:
        if member in S2R.keys():
            EcoS2R[member]=S2R[member]
    return EcoS2R
#print EcoS2R

def drawEmail(dict):
    dg = nx.DiGraph();
    for u in dict.keys():
        for v in dict.get(u):
            t=u
            if ',' in u:
                t=u.split(',')[1]
            if ',' in v:
                v=v.split(',')[1]
            #print u + ' ----> ' + v   
            dg.add_edge(t, v) 
            #nx.draw_networkx(dg,node_size=100,node_color='r',edge_color='b') 
            #plt.show()
            #plt.close()
            #time.sleep(0.1)
            #nx.draw_circular(dg,node_size=100,node_color='r',edge_color='b')
    nx.draw(dg,node_size=300,node_color='r',edge_color='b',alpha=0.5,label="EcoSys2's Email Network")
    plt.show()
def reduceHelper(x,y):
    if ';' in y:
        x.extend(y.split(';'))
    else:
        x.append(y)
    return x
