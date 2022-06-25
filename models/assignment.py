from models.dbConnection import DatabaseConnection

class Assignment:
    __db = DatabaseConnection()
    __conn = __db.get_conn()
    __cursor = __db.get_cursor()
    __question_id = ""
    __user_id = ""
    __answer = ""
    
    def __init__(self, question_id, user_id, answer):
        self.__question_id = question_id
        self.__user_id = user_id
        self.__answer = answer
        sql = "INSERT INTO `answers_rawan`( `question_id`, `user_id`, `answer`) VALUES (%s, %s, %s)"
        val = (self.__question_id, self.__user_id, self.__answer)    
        self.__cursor.execute(sql, val)
        self.__conn.commit()  
        print("__init__")
        
