from flask import  redirect, render_template, request, url_for
from flask import session
from models.quiz import Quiz

class QuizesController:

    def submit_quizes_form(self):
        if request.method == "POST":
            print("form questions", str(request.form.getlist('question')))
            print("form answers", str(request.form.getlist('answer')))
            
            questions = request.form.getlist('question')
            answers = request.form.getlist('answer')
            for i in range(len(questions)):
               quiz =  Quiz(questions[i], session['id'], answers[i])
            return redirect(url_for("courses"))
    # def submit_question_bank(self):
        
