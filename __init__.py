from flask import Flask, render_template,request
from flask import session
import os
from test import *
from controllers.userController import UserController
userController = UserController()

from controllers.courseController import CourseController
courseController = CourseController()

from controllers.assignmentController import AssignmentController
assignmentController = AssignmentController()

from controllers.quizesController import QuizesController
quizesController = QuizesController()

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

@app.route("/profile")
def profile():
    return userController.profile()

@app.route("/courses")
def courses():
    return courseController.courses()

@app.route("/coursechoice/<course_id>")
def course_choice(course_id):
    return courseController.course_choice(course_id)

@app.route("/coursechoice/assignments/<course_id>")
def course_choice_assignments(course_id):
    return courseController.course_choice_assignments(course_id)

@app.route("/coursechoice/quizes/<course_id>")
def course_choice_quizes(course_id):
    return courseController.course_choice_quizes(course_id)

@app.route("/coursechoice/assignments/assignment_question/<assignment_id>")
def selected_assignment_question(assignment_id):

    return courseController.selected_assignment_question(assignment_id)

@app.route("/coursechoice/assignments/assignment_question/",methods=['POST'])
def getdata():
    ans = request.form['answer']
    ref_ans = request.form['refrance_ans']
    print(ans)
    print(ref_ans)
    acc =test(ref_ans, ans)
    return render_template("show data.html", acc=acc)

@app.route("/submit_form", methods= ['GET', 'POST'])
def submit_form():
    return assignmentController.submit_form()

@app.route("/submit_quizes_form", methods= ['GET', 'POST'])
def submit_quizes_form():
    return quizesController.submit_quizes_form()

@app.route("/instructor_feedback", methods=['POST', 'GET'])
def instructor_feedback():
    return userController.instructor_feedback()

@app.route("/questionbank", methods=['POST', 'GET'])
def questionbank():
     return userController.questionbank()

@app.route("/transcript")
def transcript():
    return userController.transcript()

@app.route("/instructorCourses")
def instructorCourses():
    return userController.InstructorCoursess()

@app.route("/sendemail", methods=['POST', 'GET'])
def sendemail():
    return userController.sendemail()
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

@app.route("/removeuser/<user_id>")
def removeuser(user_id):
    print("Mostafa", user_id)
    return userController.removeuser(user_id)

@app.route("/adminuser")
def userType():
    return userController.adminuser()

@app.route("/addinstructor", methods=['POST', 'GET'])
def addinstructor():
    return userController.addinstructor()
    
@app.route("/logout")
def logout():
    session.pop('id', None)
    return userController.signin()


if __name__ == "__main__":
    app.run(debug=True)