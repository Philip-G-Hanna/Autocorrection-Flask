from models.dbConnection import DatabaseConnection

class classAssignment:
    db_connection = DatabaseConnection()
    __conn = db_connection.get_conn()
    __cursor = db_connection.get_cursor()
    __id = None
    __text= None

    def getQuestionText(self):
        return self.__id

    def addQuestionModelAnswer(self,text,answer):
        self.__text = text
        self.__answer = answer

        sql = "INSERT INTO `questions`(`text`,`modelanswer`) VALUES (%s,%s)"
        val = (self.__text)  
        self.__cursor.execute(sql, val)
        self.__conn.commit()  
        print("Question Added")