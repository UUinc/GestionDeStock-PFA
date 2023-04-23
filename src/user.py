from connect import *
from utils import *

class User:
    def __init__(self, username, first_name, last_name, email, password):
        self.__username = username
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = password
        
    @staticmethod
    def login(username, password):
        conn = mysqlconnect()
        cur = conn.cursor()
        cur.execute('SELECT count(*) FROM User WHERE username = %s AND password = %s', (username, password))
        output = cur.fetchone()
        conn.close()
        return output[0]==0
        
    def signup(self):
        conn = mysqlconnect()
        cur = conn.cursor()
        try:
            cur.execute('INSERT INTO user VALUES(%s, %s, %s, %s, %s)', (self.__username, self.__first_name, self.__last_name, self.__email, self.__password))
            conn.commit()
            print('new user added')
            return True
        except Exception as e:
            match e.args[1].split()[5].strip('\''):
                case 'PRIMARY':
                    print("Username already exist")
                case 'UC_email':
                    print("Email already exist")
                case _:
                    print("error occured!")
            return False
        conn.close()

    @staticmethod
    def get_information(username):
        conn = mysqlconnect()
        cur = conn.cursor()
        cur.execute('SELECT * FROM user WHERE username = %s', username)
        result = cur.fetchone()
        user = User(result[1], result[2], result[3], result[4])
        user.__username(result[0])
        conn.close()
        return user
         
    def set_information(self,first_name,last_name,email,password):
        self.__first_name=first_name
        self.__last_name=last_name
        self.__email=email
        self.__password=password


#u = user('yousra1','yousra','elbq','yous@gmail.com','456')
#u.login()
User.login('ouass1','123')
User.signup('yaya', 'yahya', 'lazrek', 'yaya@gmail.com', 'ya12')