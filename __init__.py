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

if __name__ == "__main__":
    app.run()