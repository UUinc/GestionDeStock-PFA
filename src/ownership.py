from src.connect import *
from src.utils import *

class Ownership:
    __username=''
    __stock_id=-1

    def __init__(self, username, stock_id, role):
        self.__username=username
        self.__stock_id=stock_id
        self.__ownership_start_date=current_timestamp()
        self.__role=role

    def set_username(self, username):
        self.__username = username

    def set_stock_id(self, stock_id):
        self.__stock_id = stock_id
    
    def set_ownership_start_date(self, ownership_start_date):
        self.__ownership_start_date = ownership_start_date

    def change_role(self, role):
        self.__role = role
        self.__ownership_start_date=current_timestamp()

    def get_role(self):
        return self.__role

    @staticmethod
    def get_ownership(username, stock_id):
        conn = mysqlconnect()
        cur = conn.cursor()
        cur.execute('SELECT * FROM stockownership WHERE username = %s and stock_id = %s', (username, stock_id))
        result = cur.fetchone()
        ownership = Ownership(result[0], result[1], result[3])
        ownership.set_ownership_start_date(result[2])
        conn.close()
        return ownership

    def add_stock_user(self):
        conn = mysqlconnect()
        cur = conn.cursor()
        try:
            cur.execute('''INSERT INTO stockownership(username, stock_id, ownership_start_date, role) 
                       VALUES(%s, %s, %s, %s)''', 
                    (self.__username, self.__stock_id, self.__ownership_start_date, self.__role))
            conn.commit()
            print('new stock user added')
            return True
        except Exception as e:
            if e.args[0] == 1452:
                match e.args[1].split()[17].strip('(').strip(')').strip('`'):
                    case 'username':
                        print("Username does not exist")
                    case 'stock_id':
                        print("Stock id does not exist")
                    case _:
                        print("error occured!")
            elif e.args[1].split()[5].strip('\'') == "PRIMARY":
                print("Primary key already exist")
            return False
        conn.close()

    def remove_stock_user(self):
        conn = mysqlconnect()
        cur = conn.cursor()
        cur.execute('DELETE FROM stockownership WHERE stock_id = %s and username= %s',self.__stock_id, self.__username)
        conn.commit()
        print('stock user removed')
        conn.close()

    def edit_stock_user(self):
        conn = mysqlconnect()
        cur = conn.cursor()
        cur.execute('''UPDATE stockownership 
                       SET ownership_start_date = %s, role = %s 
                       WHERE stock_id = %s and username= %s
                    ''', (self.__ownership_start_date, self.__role, self.__stock_id, self.__username))
        conn.commit()
        print('stock user updated')
        conn.close()

    @staticmethod
    def get_users(username):
        conn = mysqlconnect()
        cur = conn.cursor()
        cur.execute('SELECT s.* FROM stockownership AS o JOIN stock AS s ON o.stock_id = s.stock_id WHERE o.username = %s', username)
        result = cur.fetchall()
        conn.close()
        return result
    
    @staticmethod
    def get_users(stock_id):
        conn = mysqlconnect()
        cur = conn.cursor()
        cur.execute('SELECT o.username, u.email, o.role FROM stockownership AS o JOIN user AS u ON u.username = o.username WHERE stock_id = %s',stock_id)
        result = cur.fetchall()
        conn.close()
        return result

test = Ownership("yousra.eb", 3, "edit")
test.add_stock_user()