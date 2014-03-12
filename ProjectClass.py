'''
Created on Feb 27, 2014

@author: CT61557
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os.path
import sys

class ProjectAnalysis:
    #class variable counts the number of projects
    projectsNum = 0;
    FileTeamMembers = 'TeamMembers.txt'
    DEBUG = False;
    def __init__(self,projectDir,site,PRtraffic,KPTraffic=None):
        projectDir = projectDir.strip()
        self.projectDir = projectDir
        site = site.lower()
        site = site.replace('%20',' ')
        self.path='./../result/' + projectDir 
        if not os.path.isdir(self.path):
            os.mkdir(self.path);
        self.projectURL=site
        ProjectAnalysis.projectsNum +=1
        f=open(self.path + '/AnalysisReport.txt','w+')
        f.write('PROJECT ANALYSIS REPORT for projectDir:\n\n\n')
        f.write('Project Site: ' + site +'\n\n')
        f.close()
        #PROJECT REPOSITORY ANALYSIS
        self.loadTeamMembers()
        self.getPRVisitHistory(PRtraffic)
        self.PRusers2time = {}
        self.rankTopVisitors(self.PRresult,self.PRusers2time)
        self.getNoneVisitors(self.PRusers2time,'Project Repository')
        self.pieChart(self.PRusers2time,'Project Repository')
        # self.historyHistogram()
       
        #PROJECT KNOWLEDGE PORTAL ANALYSIS
        self.getKPVisitHistory(KPTraffic)
        self.KPusers2time = {}
        self.rankTopVisitors(self.KPresult,self.KPusers2time)
        self.pieChart(self.KPusers2time,'Knowledge Portal')
        self.getNoneVisitors(self.KPusers2time,'Knowledge Portal')
    def loadTeamMembers(self):
        try:
            f = open(self.path +'/' + ProjectAnalysis.FileTeamMembers)
        except IOError:
            sys.stderr.write('IOError: File "' +  self.path +'/' + ProjectAnalysis.FileTeamMembers + '" does not exist')
            sys.stderr.write('\nPlease put this file back and then try again')
            sys.exit(0)
        names= f.readlines()
        members=[]
        self.name2acount={}
        self.acount2name={}
        miss=[]
        if(ProjectAnalysis.DEBUG):
            print names
        for name in names:
            name = name.rstrip('\n')
            name=name.strip()
            if len(name) ==0:
                continue
            members.append(name)
        try:
            usernameRecords=pd.read_csv('../data/usersName.csv')
        except IOError:
            sys.stderr.write('IOError: File "' +  '../data/usersName.csv' + '" does not exist')
            sys.stderr.write('\nPlease put this file back and then try again')
            sys.exit(0)
        usernameRecords.index=usernameRecords.USERNAME
        usernameRecords=usernameRecords.drop(['Unnamed: 0','USERNAME'],axis=1)
        #print usernameRecords.head(10)
        for username in members:
            try:
                acount = usernameRecords.ix[username]
                acount = acount.values
                if len(acount) ==1:
                    self.name2acount[username]=acount
                elif len(acount) >1:
                    lst=[]
                    for c in acount:
                        lst.append(c[0])
                    self.name2acount[username]=lst
                for acount in self.name2acount[username]:
                    self.acount2name[acount]=username
            except KeyError:
                miss.append(username)
        f=open(self.path + '/AnalysisReport.txt','a+')
        f.write("There are total: "+str(len(members))+' Team members\n')
        if len(miss)>0:
            f.write('There are '+str(len(miss))+" Member's MM acount missing:\n")
            f.write('                ')
            f.writelines(miss)
            f.write('\n')
        if(ProjectAnalysis.DEBUG):
            print 'They are: ', miss
        f.close()
    # calculate the PR visit history of this project team members  
    def getPRVisitHistory(self,traffic):
        PRResult = 'PRResult.csv'
        PRMediateData = 'PRTeamMembersVisitsLog.csv'
        if(ProjectAnalysis.DEBUG):
            print '\nFUNCTION: getPRVisitHistory'
        if os.path.isfile(self.path+ '/'+PRResult):
            self.PRresult = pd.read_csv(self.path+ '/'+PRResult)
            if(ProjectAnalysis.DEBUG):
                print 'VisitHistory load from existing file: ' + self.path+ '/'+PRResult
            return
        users=self.acount2name.keys()
        #filter out these non team member rows 
        ls = traffic.UserMM.map(lambda x: x in users).values
        self.PRresult = traffic.loc[ls]
        self.PRresult.to_csv(self.path+'/' + PRMediateData)
        # filter out these row which has no relationship with this projects
        if(ProjectAnalysis.DEBUG):
            print 'Rows after non team members filtering: ', len(self.PRresult.Date), ' rows'
        ls=self.PRresult.Page.map(lambda x : x.startswith(self.projectURL))
        self.PRresult = self.PRresult[ls]
        # print self.PRresult.columns
        # self.PRresult = self.PRresult.drop('Unnamed: 0',axis=1);
        self.PRresult.index=range(0,len(self.PRresult.Date))
        self.PRresult['Name']=self.PRresult['UserMM'].map(lambda x : self.acount2name[x])
        cols=['Date','Name','UserMM','Page','Visits','Views']
        self.PRresult=self.PRresult[cols]
        self.PRresult.to_csv(self.path+'/' + PRResult)
        #print self.PRresult.columns
        if(ProjectAnalysis.DEBUG):
            print 'Rows after non site filtering: ', len(self.PRresult.Date), ' rows'
        f=open(self.path + '/AnalysisReport.txt','a+')
        f.write('Project Repository:  ' + str(len(self.PRresult.Date)) + ' times visits\n')
        f.close()
    # calculate the PR visit history of this project team members  
    def getKPVisitHistory(self,traffic):
        KPResult = 'KPResult.csv'
        if(ProjectAnalysis.DEBUG):
            print '\nFUNCTION: getKPVisitHistory'
        if os.path.isfile(self.path+ '/'+KPResult):
            self.KPresult = pd.read_csv(self.path+ '/'+KPResult)
            if(ProjectAnalysis.DEBUG):
                print 'VisitHistory load from existing file: ' + self.path+ '/'+KPResult
            return
        users=self.acount2name.keys()
        ls = traffic.UserMM.map(lambda x: x in users).values
        self.KPresult = traffic.loc[ls]
        # print self.KPresult.columns
        # self.KPresult = self.KPresult.drop('Unnamed: 0',axis=1);
        self.KPresult.index=range(0,len(self.KPresult.Date))
        self.KPresult['Name']=self.KPresult['UserMM'].map(lambda x : self.acount2name[x])
        cols=['Date','Name','UserMM','Page','Visits','Views']
        self.KPresult=self.KPresult[cols]
        self.KPresult.to_csv(self.path+'/' + KPResult)
        f=open(self.path + '/AnalysisReport.txt','a+')
        f.write('Knowledge Portal' + str(len(self.KPresult.Date)) + ' times visits\n')
        f.close()
        
        # rank the top visitors 
    def rankTopVisitors(self,result,users2time):
        if(ProjectAnalysis.DEBUG):
            print '\nFUNTION: rankTopVisitors'
        users = result.UserMM
        users = list(users)
        if(ProjectAnalysis.DEBUG):
            print users
        for user in users:
            if users2time.has_key(self.acount2name[user]):
                users2time[self.acount2name[user]] = users2time[self.acount2name[user]]+1
            else:
                users2time[self.acount2name[user]]=1
        #f=open(self.path + '/AnalysisReport.txt','a+')
        #f.write('Top Visitors of Project Reporsitory:\n')
        #for user in self.users2time.keys():
        #    f.write('\t' + user + ' : ' + str(self.users2time[user]) +'\n')
        #f.close()
    def pieChart(self,user2time, chartTitle):
        if(ProjectAnalysis.DEBUG):
            print '\nFUNTION: pieChart'
        # Team Member Visits Rate Of PROJECT REPOSITORY
        fig= plt.figure(figsize=(20, 7))
        fig.suptitle(self.projectDir, fontsize=18, fontweight='bold')
        visits = user2time.values()
        users = user2time.keys()
        visits.sort()
        visits.reverse()
        names =[]
        temp = list(set(visits))
        temp.sort()
        temp.reverse()
        for val in temp:
            for user in users:
                if user2time[user] == val:
                    names.append(user)
        pos = np.arange(len(visits))
        plt.title('Team Member Visits Rate of ' + chartTitle)
        plt.barh(pos, visits,color='red')
        plt.yticks(pos + .5, names)
        #add the numbers to the side of each bar
        for p, c, ch in zip(pos, names, visits):
            plt.annotate(str(ch), xy=(ch + 1, p + .5), va='center')
        #set plot limits
        plt.ylim(pos.max()+1, pos.min() - 1)
        maxWid = max(visits)
        plt.xlim(0, int(1.05 * maxWid))
        if(ProjectAnalysis.DEBUG):
            print 'Dir Path: ', self.path
        fig.text(0.95, 0.01, self.inactiveMembers,
        verticalalignment='bottom', horizontalalignment='right',
       # transform=fig.transAxes,
        color='green', fontsize=15)
        plt.savefig(self.path+ '/' + chartTitle +' visitsRate')
        #plt.show()
        
        
    def getNoneVisitors(self,users2time,title):
        if(ProjectAnalysis.DEBUG):
            print '\nFUNTION: getNoneVisitors ' + title
        # show the team members who didn't visited project site
        sets=set(self.acount2name.values());
        subsets=users2time.keys()
        if(ProjectAnalysis.DEBUG):
            print 'users num: ', len(sets), '  ', len(subsets)
        negativeMembers=[];
        self.inactiveMembers = negativeMembers
        for member in sets:
            if not member in subsets:
                negativeMembers.append(member)
                #print member
        f=open(self.path + '/AnalysisReport.txt','a+')
        if len(negativeMembers) != 0:
            f.write('\nThese members did NOT visit ' + title + ': \n')
            for member in negativeMembers:
                f.write('\t' + member +'\n')
        else:
            f.write('\nAll team members involved in ' + title  +'\n')
        f.close()
    def historyHistogram(self):
        if(ProjectAnalysis.DEBUG):
            print '\nFUNTION: historyHistogram'
        plt.figure()
        # draw visit history Histogram
        dateStrs = self.PRresult.Date.values
        months=[]
        self.dic={}
        for date in dateStrs:
            index = date.find('/')
            month= int(date[:index])
            rest = date[index+1:]
            index = rest.find('/')
            year = rest[index+1:]
            monthYear = str(month) + '/'+ year
            if self.dic.has_key(monthYear):
                self.dic[monthYear]=self.dic[monthYear]+1
            else:
                self.dic[monthYear]=1
            months.append(month)
        if(ProjectAnalysis.DEBUG):
            print months
        n, bins, patches = plt.hist(months, 2, facecolor='g', alpha=0.8)
        plt.xlabel('Month')
        plt.ylabel('Visits frequency')
        plt.title('Project Site Visit History')
        #plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
        plt.axis([4, 12, 0, 100])
        plt.grid(True)
        plt.savefig(self.path+'/ProjectSiteVisitHistory')