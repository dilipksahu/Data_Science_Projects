#!python
print("content-type:text/html \r\n\r\n")

head='''
    <center>
      <table border=1 width=40% >
	    <tr>
		    <td>ID</td>
			<td>Name</td>
			<td>Contact</td>
			<td>Email ID</td>
			<td>Edit</td>
			<td>View</td>
			<td>Delete</td>
		</tr>
        </center>

'''

print(head)

print("<center><h2><a href='form.py' >INSERT</a> | <a href='display.py'>VIEW RECORDS</a> | <a href='logout.py?user={}'>LOGOUT</a></h2></center>")

import pymysql

servername="localhost"
username="root"
password=""
dbname="todo"

db=pymysql.connect(servername,username,password,dbname)


if db:
  
   print("<center><h2>Summary Of Available Records</h2>")
   cur=db.cursor()
   query="select * from student"
   
   cur.execute(query)
   
   data=cur.fetchall()
   
   for row in data:
        
          print("<tr>")
		  
          print("<td>{}</td>".format(row[0]))
          print("<td>{}</td>".format(row[1]))
          print("<td>{}</td>".format(row[2]))
          print("<td>{}</td>".format(row[4]))
          print("<td><a href='edit.py?id={}'>Edit</a></td>".format(row[0]))
          print("<td><a href='view.py?id={}'>View</a></td>".format(row[0]))
          print("<td><a href='delete.py?id={}'>Delete</a></td>".format(row[0]))
          print("</tr>") 
        
    
else:

   print("<h1>Error in connection</h1>")

foot="</table>"
print(foot)	
