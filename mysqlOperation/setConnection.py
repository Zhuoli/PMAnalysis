'''
Created on Apr 17, 2014

@author: CT61557
'''
import MySQLdb as msq
import os
import sys
import FilePaths

PROJECT_TABLE = FilePaths.PROJECT_TABLE
MEMBER_TABLE = FilePaths.PERSON_TABLE
ROLE_RELATION_TABLE = FilePaths.ROLE_RELATION_TABLE
ROLE_TABLE = FilePaths.ROLE_TABLE

# set up connecction to my local mysql and return the pip
def getConnection(HostName = "127.0.0.1",PORT = 3306,USERNAME="root",PASSWD="cp8482617",DATABASE='knowledgeeco'):
    conn=msq.Connect(host=HostName,user=USERNAME,passwd=PASSWD,db=DATABASE,port=PORT)
    return conn

# create table
def createTable(conn):
    try:
        cur=conn.cursor()
        project_sql="create table if not exists " + PROJECT_TABLE + "(\
                                                        Name varchar(255) not null,\
                                                        Alias varchar(255) not null,\
                                                        ManagerID varchar(255),\
                                                        StartDate varchar(255),\
                                                        ProjectSite varchar(255),\
                                                        PRIMARY KEY (Alias)\
                                                        )"

        member_sql="create table if not exists " + MEMBER_TABLE + "(\
                                                        MMID varchar(125) not null,\
                                                        name varchar(32) not null,\
                                                        PRIMARY KEY (MMID)\
                                                        )"
        role_relation_sql="create table if not exists " + ROLE_RELATION_TABLE + "(\
                                                        ProjectID varchar(255) not null,\
                                                        MMID      varchar(125) not null,\
                                                        Role      varchar(32) not null,\
                                                        PRIMARY KEY (ProjectID,MMID,Role),\
                                                        CONSTRAINT"\
                                                     +" FOREIGN KEY (ProjectID) REFERENCES " + PROJECT_TABLE +"(Alias),"\
                                                     +" FOREIGN KEY (MMID) REFERENCES " + MEMBER_TABLE + "(MMID),"\
                                                     +" FOREIGN KEY (Role) REGFERENCES " + ROLE_TABLE + "(Role))"
        role_sql="create table if not exists " + ROLE_TABLE + "(\
                                                        Role    varchar(32) not null,\
                                                        PRIMARY KEY (Role))"
        #print sql
        cur.execute(project_sql)
        cur.execute(member_sql)
        cur.execute(role_sql)
        cur.execute(role_relation_sql)
        cur.close();
        conn.close()
    except msq.Error,e:
        print "Mysql Error %d: %s " %(e.args[0],e.args[1])

def projectsInsertAliaNames(conn):
    root='../../result'
    aliaNames = os.listdir(root)
    try:
        cur=conn.cursor()
        for alianame in aliaNames:
            sql = 'INSERT INTO ' + PROJECT_TABLE + " (name,alias) values (%s,%s)"
            cur.execute(sql,(alianame,alianame))
            # commit your changes in the database
            conn.commit()
        cur.close()
        conn.close()
    except msq.Error,e:
        print "Mysql Error %d: %s " %(e.args[0],e.args[1])

def project_member_Insert(conn):
    root='../../result'
    aliases = os.listdir(root)
    try:
        cur=conn.cursor()
        tableID=1
        for alias in aliases:
            members = getTeamMembers(root,alias)
            for member in members:
                sql = 'INSERT INTO ' + MEMBER_TABLE + " (tableID,project,member) values (%s,%s,%s)"
                data=(tableID,alias,member)
                tableID=tableID+1;
                cur.execute(sql,data)
                # commit your changes in the database
                conn.commit()
            path=root+'/'+alias+'/charts/tables'
            excels=os.listdir(path)
            
        cur.close()
        conn.close()
    except msq.Error,e:
        print "Mysql Error %d: %s " %(e.args[0],e.args[1])

def getTeamMembers(dir,project):
    path =dir + "/"+project+"/"+FilePaths.FileTeamMembers
    try:
        f = open(path)
    except IOError:
        sys.stderr.write('IOError: File "' + path + '" does not exist')
        sys.stderr.write('\nPlease put this file back and then try again')
        sys.exit(0)
    names= f.readlines()
    members=[]
    for name in names:
        name = name.rstrip('\n')
        name=name.strip()
        if len(name) ==0:
            continue
        members.append(name)
    return members




createTable(getConnection())
#projectsInsertAliaNames(getConnection())
#project_member_Insert(getConnection())

# conn = getConnection()
# cur=conn.cursor()
# try:
#     sql="SELECT * FROM project"
#     cur.execute(sql)
#     results=cur.fetchall()
#     for row in results:
#         print row
# except Exception, e:
#     print e
# cur.close()
# conn.close()
#print sql % ('"AcordStandardsUpdate"','"AcordStandardsUpdate"')
