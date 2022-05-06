from flask import Flask, redirect, render_template, request, url_for

from models.user import User 

user = User()

app = Flask(__name__)

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

@app.route("/signup", methods=['POST', 'GET'])
def signup():
    # global msg
    if request.method == "POST":
        user.addUser(request.form['fname'], request.form['lname'], request.form['email'], request.form['phone'], request.form['password'], request.form['age'])
        #!VALIDATION??#
        return redirect(url_for("homepage"))
    return render_template("signup.html")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/instructorprofile")
def instructorprofile():
    return render_template("instructorprofile.html", fn=user.getFname(),ln=user.getLname(),email=user.getEmail(),pn=user.getPhoneNumber())

@app.route("/studentprofile")
def studentprofile():
    return render_template("studentprofile.html")

@app.route("/questionbank")
def questionbank():
    return render_template("questionbank.html")

@app.route("/studentprofile")
def studentprofile():
    return render_template("studentprofile.html", fn=user.getFname(),ln=user.getLname(),email=user.getEmail(),pn=user.getPhoneNumber(), pw=user.getPassword())
    
if __name__ == "__main__":
    app.run()