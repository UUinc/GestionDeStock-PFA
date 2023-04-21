from connect import *
from utils import *

class Ownership:
    __username=''
    __stock_id=-1
    def __init__(self,role):
        self.__ownership_start_date=current_timestamp()
        self.__role=role

    def add_stock_user(self):
        conn = mysqlconnect()
        cur = conn.cursor()

        cur.execute('''INSERT INTO stockownership(username,stock_id,ownership_start_date,role) 
                       VALUES(%s, %s, %s, %s)''', 
                    (self.__stock_id,self.__username,self.__ownership_start_date,self.__role))
        conn.commit()
        print('new stock user added')
        
        conn.close()

    def remove_stock_user(self):
        conn = mysqlconnect()
        cur = conn.cursor()
    
        cur.execute('DELETE FROM stockownership WHERE stock_id = %s and username= %s',self.__stock_id,self.__username)
        conn.commit()
        print('stock user removed')
        
        conn.close()
    def edit_stock_user(self):
        conn = mysqlconnect()
        cur = conn.cursor()

        cur.execute('''UPDATE stockownership 
                       SET ownership_start_date = %s, role = %s 
                       WHERE stock_id = %s and username= %s
                    ''', (self.__ownership_start_date,self.__role))
        conn.commit()
        print('stock user updated')
        
        conn.close()