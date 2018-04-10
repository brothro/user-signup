from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)


app = Flask(__name__)

app.config['DEBUG'] = True 


@app.route("/signedup", methods=['POST'])
def sign_up():
    valid_sign_up = request.form['username']
    username = str(request.form['username'])
    password = str(request.form['password'])
    verify = str(request.form['verify'])
    email = str(request.form['email'])

    stripped_username = username.replace(" ", "")
    username_error = ""

    if username == "":
        username_error = "That's not a valid username"
        
    if len(username) < 3 or len(username) > 20:
        username_error = "That's not a valid username"
    
    if stripped_username != username:
        username_error = "That's not a valid username"
    
    stripped_password = password.replace(" ", "")
    password_error = ""   
     
    if password == "":
        password_error = "That's not a valid password"
        
    if len(password) < 3 or len(password) > 20:
        password = "That's not a valid password"
    
    if stripped_password != password:
        password_error = "That's not a valid password"

    stripped_verify = verify.replace(" ", "")
    verify_error = ""

    if verify == "":
        verify_error = "That's not a valid password"

    if verify != password:
        verify_error = "Passwords do not match"
    
    stripped_email = email.replace(" ", "")
    email_error = ""

    if stripped_email != email:
        email_error = "That's not a valid email"
    
    if email == "":
        email_error = ""
    else:
        at_sign = email.find("@")
        period = email.find(".")

        if at_sign == -1 or period == -1:
            email_error = "That's not a valid email"

    error = username_error + password_error + verify_error + email_error

    if error == "":
        return render_template('signed-up.html', valid_sign_up=valid_sign_up)
    else:
        template = jinja_env.get_template('user-signup.html')
        return template.render(username=username, email=email, username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)

    


@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('user-signup.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()