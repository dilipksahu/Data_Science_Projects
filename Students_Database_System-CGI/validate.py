#!python
print("content-type:text/html \r\n\r\n")

import cgi
data=cgi.FieldStorage()

u=data.getvalue('username')
p=data.getvalue('password')

user="dilipsahu"
passwd="123456"
print("Username: ",user,"<br>")
print("Password: ",passwd)
if user == u and passwd == p:
    print("<h1>You have  Login Successfully....!</h1>")
    print("<a href='form.py' >INSERT</a> | <a href='display.py'>VIEW RECORDS</a> | <a href='logout.py'>LOGOUT</a>")
else:
    print("<h1>Sorry, Login failed ....!</h1>")
    print("<a href='login.py' >To Login</a>")