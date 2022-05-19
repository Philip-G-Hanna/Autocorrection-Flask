
from flask import Flask
from flask import  redirect, render_template, request, url_for
from flask import session
import os
from controllers.userController import UserController
userController = UserController()

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/signin", methods=['POST', 'GET'])
def signin():
    return userController.signin()

from flask import Flask, redirect, render_template, request, url_for
from flask import session
import os
from models.user import User 
from controllers.userController import UserController
userController = UserController()
user = User()

app = Flask(__name__)
app.secret_key = os.urandom(24)

msg = ''

@app.route("/signin", methods=['POST', 'GET'])
def signin():
    global msg
    if request.method == "POST":

        account = user.login(request.form['email'], request.form['password'])

        if(account and user.getType() == 1): #student
            return render_template("index.html", utype=1)
        elif(account and user.getType() == 2): #instructor
            return render_template("index.html", utype=2)
        elif(account and user.getType() == 3): #admin
            return render_template("admin.html", utype=3)
        else:
            msg = "Incorrect email/password"
            
    return render_template("signin.html", msg=msg)

@app.route("/signup", methods=['POST', 'GET'])
def signup():
    return userController.signup()

@app.route("/")
def index():
    return userController.index()

@app.route("/instructor_feedback", methods=['POST', 'GET'])
def instructor_feedback():
    return userController.instructor_feedback()

@app.route("/profile")
def profile():
    return userController.profile()

@app.route("/instructorprofile")
def instructorprofile():
    return render_template("instructorprofile.html")

@app.route("/questionbank")
def questionbank():
    return userController.questionbank()

@app.route("/sendemail", methods=['POST', 'GET'])
def sendemail():
    return userController.sendemail()
    
@app.route("/transcript")
def transcript():
    return userController.transcript()

@app.route("/instructorCourses")
def instructorCourses():
    return userController.InstructorCoursess()

@app.route("/logout")
def logout():
    session.pop('id', None)
    return userController.signin()
    
@app.route("/studentprofile")
def studentprofile():
    return render_template("studentprofile.html", fn=user.getFname(),ln=user.getLname(),email=user.getEmail(),pn=user.getPhoneNumber(), pw=user.getPassword())

@app.route("/admin")
def admin():
    return userController.admin()

@app.route("/adminuser")
def adminuser():
    return userController.adminuser()

@app.route("/admin_courses")
def admin_courses():
    return userController.admin_courses()

@app.route("/admin_messages")
def admin_messages():
    return userController.admin_messages()
    
@app.route("/adminuser")
def userType():
    return userController.userType()

@app.route("/addinstructor", methods=['POST', 'GET'])
def addinstructor():
    return userController.addinstructor()
   
if __name__ == "__main__":
    app.run()