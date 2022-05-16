from unittest import result
from models.dbConnection import DatabaseConnection

class Questions:
    db_connection = DatabaseConnection()
    __conn = db_connection.get_conn()
    __cursor = db_connection.get_cursor()

#hena hat7oty el attributes bta3t el table ellyu f el DB
    __questionid = None
    __questiontitle = None
    __score = None
    __studentanswer = None
    __feedback = None

    def getID(self):
        return self.__questionid

    def getfeedback(self):
        return self.__feedback

    def getQuestionTitle(self):
        return self.__questiontitle
    
    def getScore(self):
        return self.__score
    
    def getStudentAnswer(self):
        return self.__studentanswer

    def getData(self, qid, title, score,studentanswer):
        self.__questionid = qid
        self.__questiontitle = title
        self.__score = score
        self.__studentanswer = studentanswer
        

        sql = "SELECT FROM `questions`( `questionID`, `questionTitle`, `score`, `studentAnswer`) VALUES (%s, %s, %s, %s)"
        val = (self.__questionid, self.__questiontitle, self.__score, self.__studentanswer)    
        self.__cursor.execute(sql, val)
        result = self.__cursor.fetchone()
        self.__conn.commit()  
        print("Data",result)
        if(result != None):
            self.__questionid = result[0]
            self.__questiontitle= result[1]
            self.__score = result[2]
            self.__studentanswer = result[4]
        return result

    def setFeedback(self, feedback, qid):
        self.__feedback = feedback
        self.__questionid = qid


        sql = "UPDATE `questions SET feedback = (%s) WHERE questionID =(%s)"
        val = (self.__feedback, self.__questionid)    
        self.__cursor.execute(sql, val)
        self.__conn.commit()  
        print("feedbackAdded")
        return