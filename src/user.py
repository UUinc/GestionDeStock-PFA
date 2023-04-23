from connect import *
from utils import *

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

# u = User('yousra.eb','yousra','elberraq','yous@gmail.com','123')
# u.signup()

if User.login('yousra.eb','123'):
    print("Welcome")
else:
    print("Incorrect credentials")