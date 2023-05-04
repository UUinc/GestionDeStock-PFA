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
        try:
            user = User(result[0], result[1], result[2], result[3], result[4])
        except:
            user = User("", "", "", "", "")
        conn.close()
        return user
     
    @staticmethod
    def get_users(username):
        conn = mysqlconnect()
        cur = conn.cursor()
        cur.execute('SELECT s.* FROM stockownership AS o JOIN stock AS s ON o.stock_id = s.stock_id WHERE o.username = %s', username)
        result = cur.fetchall()
        conn.close()
        return result
    
    def get_firstname(self):
        return self.__first_name
    
    def get_lastname(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    #Form validation
    def verif_user(username):
        if re.match(r"^[a-zA-Z0-9_]{3,20}$", username):
            print(f"{username} is a valid username")
        else:
            print(f"{username} is not a valid username")
                
    def verif_email(email):
        if re.match(r"^(?=.{1,256}$)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            print(f"{email} is a valid email")
        else:
            print(f"{email} is not a valid email")
            
    def verif_password(password):
        if re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[/$%#@._!])[\w\d/$%#@._!]{8,20}$", password):
            print("Valid")
        else:
            print("Not valid,password must have [a-z] && [A-Z] && [0-9] && [/$%#@._!] and between 8 and 20 characters") 
