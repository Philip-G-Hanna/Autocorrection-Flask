from flask import Flask
from flask import session
import os

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

@app.route("/submit_form", methods= ['GET', 'POST'])
def submit_form():
    return assignmentController.submit_form()

@app.route("/submit_quizes_form", methods= ['GET', 'POST'])
def submit_quizes_form():
    return quizesController.submit_quizes_form()

@app.route("/instructor_feedback", methods=['POST', 'GET'])
def instructor_feedback():
    return userController.instructor_feedback()

@app.route("/questionbank")
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

@app.route("/logout")
def logout():
    session.pop('id', None)
    return userController.signin()


if __name__ == "__main__":
    app.run()