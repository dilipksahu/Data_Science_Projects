#!python
print("content-type:text/html \r\n\r\n")


content='''
    <center>
   <form method="GET" action="insert.py">
      <fieldset >
	  <legend>Student Information Form</legend>
	  <table>
	         <tr>
			      <td>Id:</td>
				  <td><input type="number" name="id"></td>
			 </tr>
			 
			 <tr>
			      <td>Full Name:</td>
				  <td><input type="text" name="name"></td>
			 </tr>
			 
			 <tr>
			      <td>Contact No.:</td>
				  <td><input type="phone" name="contact"></td>
			 </tr>
             <tr>
			      <td>City:</td>
				  <td><input type="text" name="city"></td>
			 </tr>
			 
             <tr>
			      <td>Email ID:</td>
				  <td><input type="email" name="email"></td>
			 </tr>
			 
             <tr>
			      <td>DOB:</td>
				  <td><input type="date" name="dob"></td>
			 </tr>
             
             
             <tr>
                  <td>Gender:</td>
                   <td><input type="radio" name="gender" value="male" >Male</td>
                   <td><input type="radio" name="gender" value="female">Female</td>
                  
             </tr>
                
                  
            <tr>
			      
				  <td><input type="submit" name="send" value="SAVE"></td>
				  <td><input type="reset" name="reset" value="RESET"></td>
			 </tr>
	  
	  
	  </table>
      
    </fieldset>
   </form>
    </center>
'''
print("<center><h2><a href='form.py' >INSERT</a> | <a href='display.py'>VIEW RECORDS</a> | <a href='logout.py?user={}'>LOGOUT</a></h2></center>")
print(content)
