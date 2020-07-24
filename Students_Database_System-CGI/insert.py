#!python
print("content-type:text/html \r\n\r\n")

import cgi
data=cgi.FieldStorage()

id1=data.getvalue('id')
name=data.getvalue('name')
contact=data.getvalue('contact')
city=data.getvalue('city')
email=data.getvalue('email')
dob=data.getvalue('dob')
gender=data.getvalue('gender')
 
#print("{}".format(t))
#print("{}".format(d))
#print("{}".format(date))

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
    #for row in data:
        #print(row)
    if not data:
        print("<center><h2>Operation Performed Status</h2></center>")
        query="insert into student(id,name,contact,city,email,dob,gender)values('{}','{}','{}','{}','{}','{}','{}')".format(id1,name,contact,city,email,dob,gender)
        cur.execute(query)
        db.commit()
        print("<center><h3>Data inserted successfully...!</h3></center>")
    else:
        print("<center><h2>Operation Performed Status</h2></center>")
        print("<center><h3>Record already Exist</h3></center>")
        
            
else:
    print("<center><h2>Error in connection</h2></center>")
           
