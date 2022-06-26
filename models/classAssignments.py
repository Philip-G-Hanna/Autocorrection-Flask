from models.dbConnection import DatabaseConnection

class classAssignments:
    db_connection = DatabaseConnection()
    __conn = db_connection.get_conn()
    __cursor = db_connection.get_cursor()
    __id = None
    __type = None
    __text = None
    __course_id = None
    __modelanswer = None

    def getQuestionID(self):
        return self.__id

    def getQuestionText(self):
        return self.__text

    def getQuestionModelAnswer(self):
        return self.__modelanswer
    
    def addQuestionModelAnswer(self,course_id,text,modelanswer,type,id):
        self.__text = text
        self.__modelanswer = modelanswer
        self.__id = id
        self.__course_id = course_id
        self.__type = type

        sql = "INSERT INTO `questions_rawan`(`question`,course_id,`model_answer`,type,id) VALUES (%s,%s,%s,%s,%s)"
        val = (self.__text,self.__course_id,self.__modelanswer,self.__type,self.__id)  
        self.__cursor.execute(sql, val)
        self.__conn.commit()  
        print("Question Added")