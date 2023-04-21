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
        
    def signup(self, username, first_name,last_name,email,password):
        conn = mysqlconnect()
        cur = conn.cursor()
        cur.execute('''INSERT INTO User(username, first_name, last_name, email, password)
                       VALUES(%s, %s, %s, %s, %s)''', 
                    (self.__username, self.__first_name, self.__last_name, self.__email, self.__password))
        conn.commit()
        print('Signup successful')
        conn.close()

    def get_information(self):
        pass 
    
    def set_information(self):
        pass

#u = user('yousra1','yousra','elbq','yous@gmail.com','456')
#u.login()
User.login('ouass1','123')
User.signup('yaya', 'yahya', 'lzrek', 'yaya@gmail.com', 'ya12')