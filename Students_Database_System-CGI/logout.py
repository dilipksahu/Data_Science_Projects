#!python
print("content-type:text/html \r\n\r\n")

print("<center>")
print("<h2><a href='form.py' >INSERT</a> | <a href='display.py'>VIEW RECORDS</a> | <a href='login.py'>LOGIN</a></h2>")

import cgi
data=cgi.FieldStorage()

#user=data.getvalue('user')
print("<h1>  You have Logout Successfully...!</h1>")
print("<h1>  Thankyou for Visit Us...!</h1>")
print("</center>")