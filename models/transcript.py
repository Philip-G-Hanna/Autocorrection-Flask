from models.dbConnection import DatabaseConnection
from flask import session
from flask_sqlalchemy import SQLAlchemy
class transcript:
    db_connection = DatabaseConnection()
    __conn = db_connection.get_conn()
    __cursor = db_connection.get_cursor()

    __id = None
    __coursename = None
    __coursecode = None
    __instructor = None
    __score = None
    __user_id = None
    
    
    def getID(self):
        return self.__id

    def getCourseName(self):
        return self.__coursename
    
    def getCourseCode(self):
        return self.__coursecode
    
    def getInstructor(self):
        return self.__instructor
    
    def getScore(self):
        return self.__score
    
    def getUserID(self):
        return self.__user_id

    def transcript(self,user_id):
        sql = """SELECT * FROM transcript WHERE id = """+str(user_id)+""""""
        
        self.__cursor.execute(sql, (self.__user_id))
        result = self.__cursor.fetchall()
        self.__conn.commit()
        #print("login", result)
        print("mohamed khaled",result)
        return result

    def instructorCourses(self,user_id):
        sql = """SELECT * FROM courses WHERE instructor = """+str(user_id)+""""""
        
        self.__cursor.execute(sql, (self.__user_id))
        result = self.__cursor.fetchall()
        self.__conn.commit()
        #print("login", result)
        print("mohamed khaled",result)
        return result
    