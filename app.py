<<<<<<< Updated upstream
<<<<<<< Updated upstream
from flask import Flask
from flask import session
import os
from controllers.userController import UserController
userController = UserController()

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/signin", methods=['POST', 'GET'])
def signin():
    return userController.signin()
=======
=======
>>>>>>> Stashed changes
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
        else:
            msg = "Incorrect email/password"
            
    return render_template("signin.html", msg=msg)
>>>>>>> Stashed changes

@app.route("/signup", methods=['POST', 'GET'])
def signup():
    return userController.signup()

@app.route("/")
def index():
    return userController.index()

@app.route("/instructor_feedback", methods=['POST', 'GET'])
def instructor_feedback():
    return userController.instructor_feedback()

<<<<<<< Updated upstream
<<<<<<< Updated upstream
@app.route("/profile")
def profile():
    return userController.profile()
=======
# @app.route("/studentprofile")
# def studentprofile():
#     return render_template("studentprofile.html")
>>>>>>> Stashed changes
=======
# @app.route("/studentprofile")
# def studentprofile():
#     return render_template("studentprofile.html")
>>>>>>> Stashed changes

@app.route("/questionbank")
def questionbank():
    return userController.questionbank()

@app.route("/sendemail", methods=['POST', 'GET'])
def sendemail():
    return userController.sendemail()

@app.route("/logout")
def logout():
    session.pop('id', None)
    return userController.signin()
<<<<<<< Updated upstream

<<<<<<< Updated upstream
=======
@app.route("/logout")
def logout():
    session.pop('id', None)
    return userController.signin()
=======
>>>>>>> Stashed changes
    
@app.route("/studentprofile")
def studentprofile():
    return render_template("studentprofile.html", fn=user.getFname(),ln=user.getLname(),email=user.getEmail(),pn=user.getPhoneNumber(), pw=user.getPassword())

<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
if __name__ == "__main__":
    app.run()