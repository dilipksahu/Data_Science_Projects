<<<<<<< HEAD
#!python
print("content-type:text/html \r\n\r\n")

import cgi
data=cgi.FieldStorage()

id1 = data.getvalue('id')
name = data.getvalue('name')
contact = data.getvalue('contact')
city = data.getvalue('city')
email = data.getvalue('email')
dob = data.getvalue('dob')
gender = data.getvalue('gender')

#print("{}".format(id1)) 


print("<center><h2><a href='form.py' >INSERT</a> | <a href='display.py'>VIEW RECORDS</a> | <a href='logout.py?user={}'>LOGOUT</a></h2></center>")
import pymysql

servername="localhost"
username="root"
password=""
dbname="todo"

db=pymysql.connect(servername,username,password,dbname)

if db:
   print("<center>")
   print("<h2>Operation Performed Status</h2>")
   
   cur=db.cursor()
   query="update student set name='{}', contact='{}', city='{}', email ='{}', dob ='{}', gender='{}' where id='{}'".format(name,contact,city,email,dob,gender,id1)
   cur.execute(query)
   db.commit()
   print("<h3>Data Updated Successfully...</h3>")
   print("</center>")
else:
   print("<h2>Operation Performed Status</h2>")
   print("<h1>Error in connection</h1>")
   print("</center>")
=======
#!python
print("content-type:text/html \r\n\r\n")

import cgi
data=cgi.FieldStorage()

id1 = data.getvalue('id')
name = data.getvalue('name')
contact = data.getvalue('contact')
city = data.getvalue('city')
email = data.getvalue('email')
dob = data.getvalue('dob')
gender = data.getvalue('gender')

#print("{}".format(id1)) 


print("<center><h2><a href='form.py' >INSERT</a> | <a href='display.py'>VIEW RECORDS</a> | <a href='logout.py?user={}'>LOGOUT</a></h2></center>")
import pymysql

servername="localhost"
username="root"
password=""
dbname="todo"

db=pymysql.connect(servername,username,password,dbname)

if db:
   print("<center>")
   print("<h2>Operation Performed Status</h2>")
   
   cur=db.cursor()
   query="update student set name='{}', contact='{}', city='{}', email ='{}', dob ='{}', gender='{}' where id='{}'".format(name,contact,city,email,dob,gender,id1)
   cur.execute(query)
   db.commit()
   print("<h3>Data Updated Successfully...</h3>")
   print("</center>")
else:
   print("<h2>Operation Performed Status</h2>")
   print("<h1>Error in connection</h1>")
   print("</center>")
>>>>>>> 539080ca827a98f6633dd28ae5ae9feb30e02d75
