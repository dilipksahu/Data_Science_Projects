#!python
print("content-type:text/html \r\n\r\n")

import cgi
data=cgi.FieldStorage()

id1=data.getvalue('id')
#print("<h3>{}</h3>".format(id1))

print("<center><h2><a href='form.py' >INSERT</a> | <a href='display.py'>VIEW RECORDS</a> | <a href='logout.py?user={}'>LOGOUT</a></h2></center>")

import pymysql

servername="localhost"
username="root"
password=""
dbname="todo"

db=pymysql.connect(servername,username,password,dbname)


if db:
  
   print("<center><h2> Operation Performed Status</h2></center>")
   cur=db.cursor()
   query="delete from student where id='{}'".format(id1)
   cur.execute(query)
   db.commit()
   print("<center><h3>Record deleted successfully...!</h3></center>")