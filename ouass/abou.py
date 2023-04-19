from connect import *
from utils import *
class user:
 
    def _init_(self,u,f,l,e,p):
        self.__username=u
        self.__first_name=f
        self.__last_name=l
        self.__email=e
        self.__password=p
def login():
        mesage = ''
if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        email = request.form['username']
        password = request.form['password']
        conn = mysqlconnect()
        cur = conn.cursor()
        conn.execute('SELECT * FROM user WHERE username = % s AND password = % s', (username, password ))
        conn.commit()
        

def signup( username,first_name,last_name,email,password):
        conn = mysqlconnect()
        cur = conn.cursor()

        cur.execute('''INSERT INTO user(username,first_name,last_name,email,password) 
                       VALUES(%s, %s, %s, %s, %s, %s, %s, %s)''', 
                    (self.__username,self.__first_name,self.__last_name,self.__email,self.__password))
        conn.commit()
        
        conn.close()



def getInformation():
def setInformation():