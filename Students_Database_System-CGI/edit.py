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
  
   print("<center><h1>Perform Update Operation</h1></center>")
   cur=db.cursor()
   query="select * from student where id='{}'".format(id1)
   
   cur.execute(query)
   
   data=cur.fetchall()
   
   for row in data:

        print("<center>")
        print("<form method='GET' action='update.py'>")
        print("<fieldset>")
        print("<legend>Edit Form</legend>")
        print("<table>")
        print("<tr>")
        print("<td>ID:</td>")
        print("<td><input type='number' name='id' value='{}'  readonly></td>".format(row[0]))
        print("</tr>")
        print("<tr>")
        print("<td>Full Name:</td>")
        print("<td><input type='text' name='name' value='{}'></td>".format(row[1]))
        print("</tr>")
        print("<tr>")
        print("<td>Contact:</td>")
        print("<td><input type='phone' name='contact' value='{}'></td>".format(row[2]))
        print("</tr>")
        print("<tr>")
        print("<td>City:</td>")
        print("<td><input type='text' name='city' value='{}'></td>".format(row[3]))
        print("</tr>")
        print("<td>Email Id:</td>")
        print("<td><input type='email' name='email' value='{}'></td>".format(row[4]))
        print("</tr>")
        print("<td>DOB:</td>")
        print("<td><input type='date' name='dob' value='{}'></td>".format(row[5]))
        print("</tr>")
        print("<td>Gender:</td>")
        print("<td><input type='text' name='gender' value='{}'></td>".format(row[6]))
        print("</tr>")
        print("<tr>")
        print("<td><input type='submit' name='{}' value='UPDATE' ></td>".format(row[0]))
        print("</tr>")
        print("</table>")
        print("</fieldset>")
        print("</form>")
        print("</center>")




