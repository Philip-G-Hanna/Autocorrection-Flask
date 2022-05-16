from models.dbConnection import DatabaseConnection

class classAssignment:
    db_connection = DatabaseConnection()
    __conn = db_connection.get_conn()
    __cursor = db_connection.get_cursor()
    __id = None
    __text= None

    def getQuestionText(self):
        return self.__id

    def addQuestion(self,text):
        self.__text = text

        sql = "INSERT INTO `questions`(`text`) VALUES (%s)"
        val = (self.__text)  
        self.__cursor.execute(sql, val)
        self.__conn.commit()  
        print("addQuestion")