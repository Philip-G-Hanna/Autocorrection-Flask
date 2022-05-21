from models.dbConnection import DatabaseConnection

class classAssignments:
    db_connection = DatabaseConnection()
    __conn = db_connection.get_conn()
    __cursor = db_connection.get_cursor()
    __id = None
    __text = None
    __modelanswer = None

    def getQuestionID(self):
        return self.__id

    def getQuestionText(self):
        return self.__text

    def getQuestionModelAnswer(self):
        return self.__modelanswer
    
    def addQuestionModelAnswer(self,text,modelanswer):
        self.__text = text
        self.__modelanswer = modelanswer

        sql = "INSERT INTO `questions`(`text`,`modelanswer`) VALUES (%s,%s)"
        val = (self.__text,self.__modelanswer)  
        self.__cursor.execute(sql, val)
        self.__conn.commit()  
        print("Question Added")