'''
Created on Apr 18, 2014

@author: CT61557
'''
from setConnection  import * 

conn = getConnection()
# prepare a cursor object using cursor() method
cursor = conn.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   conn.commit()
except:
   # Rollback in case there is any error
   conn.rollback()

# disconnect from server
conn.close()