
from models.dbConnection import DatabaseConnection
from flask import session

class Courses:
    db_connection = DatabaseConnection()
    __conn = db_connection.get_conn()
    __cursor = db_connection.get_cursor()
    # __id = ""
    # __name = ""
    # __description = ""
    # __image = ""

    def read_courses(self):
        sql = "SELECT * FROM courses"
        self.__cursor.execute(sql)
        result = self.__cursor.fetchall()
        self.__conn.commit()
        print("read_courses: ", result)
        return result

    def course_details(self, id):
        sql = "SELECT * FROM coursedetails WHERE id = %s"
        val = (id,)
        self.__cursor.execute(sql, val)
        result = self.__cursor.fetchone()
        self.__conn.commit()
        print("course_details: ", result)
        return result
    


    def course_questions_assigment(self, id):
        sql1 = "SELECT * FROM questions_rawan WHERE course_id = %s and Type = %s"
        val = (id,"Assigment")
        self.__cursor.execute(sql1, val)
        result = self.__cursor.fetchall()
        self.__conn.commit()
        print("course_questions: ", result)
        return result


    def course_questions_quiz(self, id):
        # sql1 = "SELECT * FROM questions_rawan WHERE course_id = %s"
        sql1 = "SELECT * FROM questions_rawan WHERE course_id = %s and Type = %s"
        val = (id,"Quiz")
        self.__cursor.execute(sql1, val)
        result = self.__cursor.fetchall()
        self.__conn.commit()
        print("course_questions: ", result)
        return result

    def course_choice_assignments(self, id):
        sql = "SELECT * FROM assignment WHERE course_id = %s"
        val = (id,)
        self.__cursor.execute(sql, val)
        result = self.__cursor.fetchall()
        self.__conn.commit()
        print("course_choice_assignment: ", result)
        return result


    def course_choice_quizes(self, id):
        sql = "SELECT * FROM quizzes WHERE course_id = %s"
        val = (id,)
        self.__cursor.execute(sql, val)
        result = self.__cursor.fetchall()
        self.__conn.commit()
        print("course_choice_quizes: ", result)
        return result

    def removecourse(self,id):
        self.__id = id
        sqldeletecourses = "DELETE FROM courses WHERE id = %s"
        self.__cursor.execute(sqldeletecourses, (self.__id,))
        self.__conn.commit()