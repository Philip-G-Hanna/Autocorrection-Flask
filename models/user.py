from mysqlx import Result
from models.dbConnection import DatabaseConnection
from flask import session
class User:
    db_connection = DatabaseConnection()
    __conn = db_connection.get_conn()
    __cursor = db_connection.get_cursor()

    __id = None
    __fname = None
    __lname = None
    __email = None
    __phoneNumber = None
    __password = None
    __dob = None
    __major = None
    __gender = None
    __type = 1
    __courseid= None



    def getID(self):
        return self.__id

    def getFname(self):
       return self.__fname

    def getLname(self):
        return self.__lname

    def getEmail(self):
        return self.__email

    def getPhoneNumber(self):
        return self.__phoneNumber

    def getPassword(self):
        return self.__password

    def getDob(self):
        return self.__dob

    def getType(self):
        return self.__type
    
    def exist_account(self, email):
        self.__email = email
        sql = """SELECT * FROM user WHERE email = %s"""
        self.__cursor.execute(sql, (self.__email,))
        result = self.__cursor.fetchone()
        self.__conn.commit()
        print("exist_account", result)
        return result  

    def register_user(self, fname,lname,email, password,gender,phonenumber,major,date):
        self.__fname = fname
        self.__lname = lname
        self.__email = email
        self.__password = password
        self.__gender = gender
        self.__phoneNumber = phonenumber
        self.__major = major
        self.__date = date

        sql = "INSERT INTO user (`fname`,lname,email, `password`,Type_id,gender,phonenumber,major,date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (self.__fname,self.__lname ,self.__email,self.__password,1,self.__gender,self.__phoneNumber,self.__major,self.__date)    
        self.__cursor.execute(sql, val)
        self.__conn.commit()  
        print("register_user")

    
    def login(self, email, password):
        self.__email = email
        self.__password = password

        sql = """SELECT * FROM user WHERE email = %s AND password = %s"""
        self.__cursor.execute(sql, (self.__email, self.__password,))
        result = self.__cursor.fetchone()
        self.__conn.commit()
        print("login", result)

        if(result != None):
            self.__id = result[0]
            self.__fname = result[1]
            self.__lname = result[2]
            self.__type  = result[5]
            self.__dob = result[7]
            self.__phoneNumber = result[8]
            session["user_id"] =result[0]
        return result
        
    def getusers(self):
        sql = "SELECT * FROM user" 
        self.__cursor.execute(sql)
        result = self.__cursor.fetchall()
        self.__conn.commit()
        return result

    def getmessages(self):
        sql1 = "SELECT * FROM contact_us" 
        self.__cursor.execute(sql1)
        result1 = self.__cursor.fetchall()
        self.__conn.commit()
        return result1

    def getcourses(self):
        sql2 = "SELECT * FROM courses" 
        self.__cursor.execute(sql2)
        result2 = self.__cursor.fetchall()
        self.__conn.commit()
        return result2

   

    def getfaculty(self):
        sql3 = "SELECT * FROM faculty" 
        self.__cursor.execute(sql3)
        result3 = self.__cursor.fetchall()
        self.__conn.commit()
        return result3
    

    def getuserType(self): 
        sql4 = "SELECT * FROM usertype" 
        self.__cursor.execute(sql4)
        result6 = self.__cursor.fetchall()
        self.__conn.commit()
        return result6

    def deletecourses(self,courseid):
        self.__courseid = courseid
        sql2 = "DELETE from courses WHERE id=%s"
        print(sql2)
        self.__cursor.execute(sql2, (self.__courseid))
        self.__conn.commit()
        # return result7

    def register_instructor(self, fname,lname,email, password):
        self.__fname = fname
        self.__lname = lname
        self.__email = email
        self.__password = password
      

        sql = "INSERT INTO user (`fname`,lname,email, `password`,Type_id) VALUES (%s, %s, %s, %s, %s)"
        val = (self.__fname,self.__lname ,self.__email,self.__password,2)    
        self.__cursor.execute(sql, val)
        self.__conn.commit()  
        print("register_instructor")

    def addquestion(self, text,modelanswer):
        sql = "INSERT INTO questions (text,modelanswer) VALUES ( %s, %s)"
        val = ("text","modelanswer")    
        self.__cursor.execute(sql, val)
        self.__conn.commit()

    def deleteuser(self,id):
        self.__id = id
        sqldeleteuser = "DELETE FROM user WHERE id = %s"
        self.__cursor.execute(sqldeleteuser, (self.__id,))
        self.__conn.commit()