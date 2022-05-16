from models.dbConnection import DatabaseConnection

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
    __type = 1

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

    def addUser(self, fname, lname, email, pn, password, dob):
        self.__fname = fname
        self.__lname = lname
        self.__email = email
        self.__phoneNumber = pn
        self.__password = password
        self.__dob = dob

        sql = "INSERT INTO `user`( `fname`, `lname`, `email`, `password`, `Type-id`, `age`, `phonenumber`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (self.__fname, self.__lname, self.__email, self.__password, self.__type, self.__dob, self.__phoneNumber)    
        self.__cursor.execute(sql, val)
        self.__conn.commit()  
        print("addUser")

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
        return result