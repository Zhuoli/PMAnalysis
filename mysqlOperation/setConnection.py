'''
Created on Apr 17, 2014

@author: CT61557
'''
HostName = "127.0.0.1"
PORT = 3306
USERNAME="root"
PASSWD="cp8482617"
DATABASE='knowledgeeco'
import MySQLdb as msq
try:
    conn=msq.Connect(host=HostName,user=USERNAME,passwd=PASSWD,db=DATABASE,port=PORT)
    cur=conn.cursor()
    cur.execute("create table projects{ ProjectName varchar(255) NOT NULL PRIMARY KEY,\
                                                       ProjectManager varchar(255),\
                                                       StartDate varchar(255 }")
    cur.close();
    conn.close()
except msq.Error,e:
    print "Mysql Error %d: %s " %(e.args[0],e.args[1])