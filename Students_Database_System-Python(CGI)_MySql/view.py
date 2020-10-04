<<<<<<< HEAD
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
  
   cur=db.cursor()
   query="select * from student where id={}".format(id1)
   
   cur.execute(query)
   
   data=cur.fetchall()
   
   for row in data:
        print("<center>")
        print("<h2> View Full Details</h2>")
        print("<table border=1 width='400px'>")
        print("<thead>")
        print("<tr>")
        print("<td>ID:</td>")
        print("<td>{}</td>".format(row[0]))
        print("</tr>")
        print("<tr>")
        print("<td>Full Name:</td>")
        print("<td>{}</td>".format(row[1]))
        print("</tr>")
        print("<tr>")
        print("<td>Contact:</td>")
        print("<td>{}</td>".format(row[2]))
        print("</tr>")
        print("<tr>")
        print("<td>City:</td>")
        print("<td>{}</td>".format(row[3]))
        print("</tr>")
        print("<tr>")
        print("<td>Email Id:</td>")
        print("<td>{}</td>".format(row[4]))
        print("</tr>")
        print("<tr>")
        print("<td>DOB:</td>")
        print("<td>{}</td>".format(row[5]))
        print("</tr>")
        print("<tr>")
        print("<td>Gender:</td>")
        print("<td>{}</td>".format(row[6]))
        print("</tr>")
        print("</thead>")
        print("</table>")
=======
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
  
   cur=db.cursor()
   query="select * from student where id={}".format(id1)
   
   cur.execute(query)
   
   data=cur.fetchall()
   
   for row in data:
        print("<center>")
        print("<h2> View Full Details</h2>")
        print("<table border=1 width='400px'>")
        print("<thead>")
        print("<tr>")
        print("<td>ID:</td>")
        print("<td>{}</td>".format(row[0]))
        print("</tr>")
        print("<tr>")
        print("<td>Full Name:</td>")
        print("<td>{}</td>".format(row[1]))
        print("</tr>")
        print("<tr>")
        print("<td>Contact:</td>")
        print("<td>{}</td>".format(row[2]))
        print("</tr>")
        print("<tr>")
        print("<td>City:</td>")
        print("<td>{}</td>".format(row[3]))
        print("</tr>")
        print("<tr>")
        print("<td>Email Id:</td>")
        print("<td>{}</td>".format(row[4]))
        print("</tr>")
        print("<tr>")
        print("<td>DOB:</td>")
        print("<td>{}</td>".format(row[5]))
        print("</tr>")
        print("<tr>")
        print("<td>Gender:</td>")
        print("<td>{}</td>".format(row[6]))
        print("</tr>")
        print("</thead>")
        print("</table>")
>>>>>>> 539080ca827a98f6633dd28ae5ae9feb30e02d75
        print("</center>")