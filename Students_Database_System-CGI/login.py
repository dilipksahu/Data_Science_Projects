#!python
print("content-type:text/html \r\n\r\n")

content='''
    <center>
    <h1> ADMIN LOGIN</h1>
    <form method="POST" action="validate.py">
        <fieldset>
            <legend>Login Form</legend>
            <table>
                <thead>
                    <tr> <td>Username:</td>
                        <td><input type="text" name="username"  ></td>
                    </tr>
                    <tr> <td>Password:</td>
                        <td><input type="password" name="password"  ></td>
                    </tr>
                    <tr>
                       
                        <td><input type="submit" name="send" value="SUBMIT"></td>
                        <td><input type="reset" name="send" value="RESET"></td>
                        <td><a href="validate.py" target="_self"> Forgot Password</a>
                    </tr>
	  
                </thead>
            </table>
        </fieldset>
    </form> 
    </center>
'''
print(content)