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

    def selected_assignment_question(self, id):
        questions = self.__courses.course_questions_assigment(id)
        model_answer = self.__courses.course_questions_assigment(id)
        return render_template("questions_assignments.html", questions=questions, model_answer=model_answer)

    def selected_quiz_question(self, id):
        questions = self.__courses.course_questions_quiz(id)
        model_answer = self.__courses.course_questions_quiz(id)
        return render_template("questions_quiz.html", questions=questions, model_answer=model_answer)


    def course_choice_assignments(self,id):
        assignments = self.__courses.course_choice_assignments(id)
        return render_template("assignments.html", assignments=assignments)

    def course_choice_quizes(self, id):
        assignments = self.__courses.course_choice_quizes(id)
        #model_answer = self.__courses.course_questions_quiz(id)
        return render_template("quizes2.html", assignments=assignments)

    def removecourse(self, course_id):
        print(course_id)
        self.__courses.removecourse(course_id)
        return redirect(url_for("admin_courses"))
