from flask import Flask, request, render_template, redirect
import cgi
import re

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
    encodederror = request.args.get("error")
    return render_template('edit.html')

@app.route("/formvalidate", methods=['POST'])
def form_validate():
    username = request.form['usrname']
    password = request.form['pwd']
    verify_pwd = request.form['vpwd']
    email = request.form['emailid']
    empty = " "
    uname_error = ""
    pwd_error = ""
    verifypwd_error = ""
    email_error = ""

    if username =="" or username ==" " or  (empty in username) == True or len(username)<3 or len(username)>20:
        uname_error = "That not a valid username"
        username = ""

    if password =="" or password ==" " or  (empty in password) == True or len(password)<3 or len(password)>20:
        pwd_error = "That not a valid password"
        password = ""
        #return render_template('edit.html',password_error = error)
    
    if verify_pwd != password:
        verifypwd_error = "Password does not match"
        verify_pwd = ""

    if email == "":
        email = ""
    else:
        regex_str = "^(?=.{3,20}$)[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+$"
        p = re.search(regex_str,email)
        if not p:
            email_error = "That is not a valid email"
            #email = ""
    
    if not uname_error and not pwd_error and not verifypwd_error and not email_error:
        return render_template('confirmation.html', username=username)
        

    return render_template('edit.html',username_error=uname_error,
        password_error=pwd_error, verifypwd_error=verifypwd_error, email_error=email_error, usrname=username, emailid=email)



app.run()

