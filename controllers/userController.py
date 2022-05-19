from flask import  redirect, render_template, request, url_for
import re
from flask import session
from models.user import User
from models.contacts import Contacts 
from models.transcript import transcript    
from models.classAssignments import classAssignment

class UserController:
    __user = User()
    __utype = 0
    __transcript = transcript()
    __classAssignment = classAssignment()
    
    def signin(self):
        msg = ''
        if request.method == "POST":
            account = self.__user.login(request.form['email'], request.form['password'])
            self.__utype = self.__user.getType()
            if(account and self.__utype == 1): #student
                session['id'] = self.__user.getID()
                return redirect(url_for("index"))
            elif(account and self.__utype == 2): #instructor
                session['id'] = self.__user.getID()
                return redirect(url_for("index"))
            else:
                msg = "Incorrect email/password"
        return render_template("signin.html", msg=msg)

    def signup(self):
        print("fname:",request.form.get('fname'))
        print(request.form.get('gender'))
        print(request.form.get('major'))
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
                self.__user.addUser(request.form.get('fname'), request.form.get('lname'), request.form.get('email'), request.form.get('phone'), request.form.get('password'), request.form.get('age'), request.form.get('gender'), request.form.get('major'))
                self.__utype = 1
                return redirect(url_for("index"))
        
        return render_template("signup.html")
    
    def index(self):
        return render_template("index.html", utype= self.__utype)

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
        return render_template("questionbank.html")
    
    def transcript(self):
        result=self.__transcript.transcript(session['id'])
        #return render_template("Transcript.html",name='result[1]',code="result[2]",instructor="result[3]",score="result[4]")
        #return render_template("Transcript.html",length=len(result),name=result[1],code=result[2],instructor=result[3],score=result[4])
        return render_template("Transcript.html",length=len(result),result=result)
    
    def InstructorCoursess(self):
        result=self.__transcript.instructorCourses(session['id'])
        return render_template("instructorCourses.html",length=len(result),result=result)