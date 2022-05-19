
from flask import  redirect, render_template, request, url_for
from flask import session, flash

from models.assignment import Assignment

class AssignmentController:
   
    def submit_form(self):
        if request.method == "POST":
            print("form questions", str(request.form.getlist('question')))
            print("form answers", str(request.form.getlist('answer')))
            
            questions = request.form.getlist('question')
            answers = request.form.getlist('answer')
            for i in range(len(questions)):
               assignment =  Assignment(questions[i], session['id'], answers[i])
            return redirect(url_for("courses"))