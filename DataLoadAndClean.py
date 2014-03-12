'''
Created on Feb 27, 2014

@author: CT61557
'''
import pandas as pd
import os.path
import sys
# <codecell>
dataDir = '../data'
###########################  SECTION itiate ########################
def removePrefix(user):
    index = user.find('\\')
    if index>0:
        return user[index+1:]
    else:
        return user
def readAndClean():
    PRTraffic = readAndCleanPR();
    KPTraffic = readAndCleanKP();
    return PRTraffic,KPTraffic

def readAndCleanKP():
    # FILE TWO
    # load the KPtraffic report and change title
    FileKPTrafiic= 'KPTraffic.csv'
    FILE_KP_DATA = 'KPDataAll.csv'
    if os.path.isfile(dataDir + '/' + FileKPTrafiic):
        print 'Traffic DataFrame load from existing file: ' + os.getcwd()+ '/data/' + FileKPTrafiic
        return pd.read_csv(dataDir + '/' + FileKPTrafiic)

    # load the PRtraffic report and change title
    try:
        KPtraffic = pd.read_csv(dataDir +'/' + FILE_KP_DATA);
    except IOError:
        sys.stderr.write('\nIOError: File "' +  dataDir +'/' + FILE_KP_DATA + '" does not exist')
        sys.stderr.write('\nPlease put this file back and then try again')
        sys.exit(0)
    KPtraffic.columns = ['Page','UserMM','Date','Hour','Views','Visits'];
    KPtraffic.UserMM = KPtraffic.UserMM.map(lambda x : removePrefix(x))
    KPtraffic.index = range(0,len(KPtraffic.Date))
    cols = ['Date','UserMM','Page','Visits','Views']
    KPtraffic=KPtraffic[cols]
    KPtraffic.to_csv(dataDir + '/' +FileKPTrafiic)
    return KPtraffic

def readAndCleanPR():
    FileLogOfVisits4PR_4_2013_12_2013 = 'PR_TrafficLog_from_4_2013.csv'
    FilePRTraffic = 'PRTraffic.csv'
    if not os.path.isdir(dataDir):
        os.mkdir(dataDir);
    if os.path.isfile(dataDir + '/' + FilePRTraffic):
        print 'Traffic DataFrame load from existing file: ' + os.getcwd()+ '/data/' + FilePRTraffic
        return pd.read_csv(dataDir + '/' + FilePRTraffic)

    # load the PRtraffic report and change title
    try:
        PRtraffic = pd.read_csv(dataDir +'/' + FileLogOfVisits4PR_4_2013_12_2013);
    except IOError:
        sys.stderr.write('\nIOError: File "' +  dataDir +'/' + FileLogOfVisits4PR_4_2013_12_2013 + '" does not exist')
        sys.stderr.write('\nPlease put this file back and then try again')
        sys.exit(0)
    PRtraffic.columns = ['Page','Visitor','UserMM','Date','Visits','Views'];
    PRtraffic = PRtraffic.drop('Visitor', axis=1);
    
    PRtraffic.UserMM = PRtraffic.UserMM.map(lambda x : removePrefix(x))
    PRtraffic.index = range(0,len(PRtraffic.Date))
    cols = ['Date','UserMM','Page','Visits','Views']
    PRtraffic=PRtraffic[cols]
    PRtraffic.to_csv(dataDir + '/' +FilePRTraffic)
    return PRtraffic
