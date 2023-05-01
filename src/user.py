from src.connect import *
from src.utils import *
import re

class User:
    def __init__(self, username, first_name, last_name, email, password):
        self.__username = username
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = hash_password(password)
        
    @staticmethod
    def login(username, password):
        conn = mysqlconnect()
        cur = conn.cursor()
        cur.execute('SELECT count(*) FROM user WHERE username = %s AND password = %s', (username, hash_password(password)))
        output = cur.fetchone()
        conn.close()
        return output[0]!=0
        
    def signup(self):
        conn = mysqlconnect()
        cur = conn.cursor()
        cur.execute('INSERT INTO user VALUES(%s, %s, %s, %s, %s)', (self.__username, self.__first_name, self.__last_name, self.__email, self.__password))
        conn.commit()
        conn.close()

    def set_information(self,first_name,last_name,email,password):
        self.__first_name=first_name
        self.__last_name=last_name
        self.__email=email
        self.__password = hash_password(password)
    
    @staticmethod
    def get_information(username):
        conn = mysqlconnect()
        cur = conn.cursor()
        cur.execute('SELECT * FROM user WHERE username = %s', username)
        result = cur.fetchone()
        user = User(result[0], result[1], result[2], result[3])
        conn.close()
        return user
    
    ####verification
    def verif_user(username):
        exp = "^[a-z A-Z 0-9]+[_]?[a-z A-Z 0-9]$"
        if re.search(exp, username):
            print(f"{username} Valid")
        else:
            print(f"{username} Not valid")
             
    
    def verif_email(email):
        exp = "^[a-z 0-9]+[\_.]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
        if re.search(exp, email ):
            print(f"{email } Valid")
        else:
            print(f"{email } Not valid")
            

    def verif_password(password):
       if(len(password)<8):
            print("Password must be 8 character long")

       if not re.search('[a-z] && [A-Z] && [0-9] && [/$%#@._]', password):
            print("Not valid,password must have [a-z] && [A-Z] && [0-9] && [/$%#@._] ") 
       else:
             print("Valid")
    
    
    
    
# u = User('yousra.eb','yousra','elberraq','yous@gmail.com','123')
# u.signup()

# if User.login('yousra.eb','123'):
#     print("Welcome")
# else:
#     print("Incorrect credentials")