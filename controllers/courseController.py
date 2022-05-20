from flask import  redirect, render_template, request, url_for


from models.courses import Courses

class CourseController:
    __courses = Courses()

    def courses(self):
        courses = self.__courses.read_courses()
        return render_template("courses.html", courses=courses)

    def course_choice(self, id):
        # coursedetails = self.__courses.course_details(id)
        # , coursedetails=coursedetails
        return render_template("coursechoice.html", id=id)

    def course_choice_assignments(self, id):
        assignments = self.__courses.course_choice_assignments(id)
        return render_template("assignments.html", assignments=assignments)

    def selected_assignment_question(self, id):
        questions = self.__courses.course_questions(id)
        return render_template("questions_assignments.html", questions=questions)

    def course_choice_quizes(self, id):
        questions = self.__courses.course_choice_quizes(id)
        return render_template("quizes.html", questions=questions)

    
    