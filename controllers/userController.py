from flask import  redirect, render_template, request, url_for
import re
from flask import session
from models.classAssignments import classAssignment
from models.user import User
from models.contacts import Contacts 

class UserController:
    __user = User()
    __classAssignment = classAssignment()
    def signin(self):
        msg = ''
        if request.method == "POST":
            account = self.__user.login(request.form['email'], request.form['password'])
            if(account and self.__user.getType() == 1): #student
                session['id'] = self.__user.getID()
                return render_template("index.html", utype=1)
            elif(account and self.__user.getType() == 2): #instructor
                session['id'] = self.__user.getID()
                return render_template("index.html", utype=2)
            else:
                msg = "Incorrect email/password"
        return render_template("signin.html", msg=msg)

    
    def signup(self):
        msg = []
        if request.method == "POST":
            account = self.__user.exist_account(request.form['email'])
            if account:
                msg.append('Account already exists!')

            if not re.match(r'[^@]+@[^@]+\.[^@]+', request.form['email']):
                msg.append('Invalid email address!')

            if not request.form['fname'].isalpha():
                msg.append('First name must contain be characters only!')

            if not request.form['lname'].isalpha():
                msg.append('Last name must contain be characters only!')

            if not request.form['phone'].isnumeric():
                msg.append('Phone number must be numbers only!')

            if not re.match(r'[A-Za-z0-9]+', request.form['password']):
                msg.append('Password must contain only characters and numbers!')

            if len(request.form['password']) < 6 :
                msg.append('Password must be at least 6 characters!')

            if request.form['password'] != request.form['rpassword']:
                msg.append('Password not match')

            if len(msg) > 0:
                return render_template("signup.html", errormsg=msg)

            # no error
            if len(msg) == 0:
                # Account doesnt exists and the form data is valid, now insert new account into accounts table
                self.__user.addUser(request.form['fname'], request.form['lname'], request.form['email'], request.form['phone'], request.form['password'], request.form['age'])
                return redirect(url_for("index", utype=self.__user.getType()))
        
        return render_template("signup.html")

        
    
    def index(self):
        return render_template("index.html")

    def sendemail(self):
        if request.method == "POST":
            contacts = Contacts(request.form['name'], request.form['email'], request.form['message'])
            contacts.send_email()
        return redirect(url_for("index"))
        
    def profile(self):
        return render_template("profile.html", fn=self.__user.getFname(),ln=self.__user.getLname(),email=self.__user.getEmail(),pn=self.__user.getPhoneNumber(), utype=self.__user.getType())
    
    def instructor_feedback(self):
        return render_template("instructor_feedback.html", fn=self.__user.getFname(),ln=self.__user.getLname(), utype=self.__user.getType())    
    
    def questionbank(self):
        return render_template("questionbank.html", text=self.__classAssignment.getQuestionText())
