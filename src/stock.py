from src.connect import *
from src.utils import *

class Stock:
    __stock_id = -1
    def __init__(self,name,description):
        self.__name=name
        self.__description=description
        self.__creation_date=current_timestamp()
        self.__last_edit=current_timestamp()

    def __str__(self):
        stock = f"Stock ({self.__stock_id})\n"
        stock += f" name: ({self.__name})\n"
        stock += f" description: ({self.__description})\n"
        stock += f" creation date: ({self.__creation_date})\n"
        stock += f" last edit: ({self.__last_edit})\n"
        return stock
    
    #setters and getters
    def set_stock_id(self, id):
        self.__stock_id = id

    def get_stock_id(self):
        return self.__stock_id

    def set_name(self, name):
        self.__name = name
        self.__last_edit=current_timestamp()

    def get_name(self):
        return self.__name

    def set_description(self,description):
        self.__description = description
        self.__last_edit=current_timestamp()

    def set_creation_date(self, creation_date):
        self.__creation_date=creation_date

    def set_last_edit(self, last_edit):
        self.__last_edit=last_edit

    #adding
    def add_stock(self):
        conn = mysqlconnect()
        cur = conn.cursor()
        cur.execute('''INSERT INTO stock(name, description, creation_date, last_edit) 
                       VALUES(%s, %s, %s, %s)''', 
                    (self.__name, self.__description, self.__creation_date, self.__last_edit))
        conn.commit()

        self.__stock_id = cur.lastrowid
        print('new stock added')
        conn.close()

    @staticmethod
    def get_stock(stock_id):
        conn = mysqlconnect()
        cur = conn.cursor()
        cur.execute('SELECT * FROM stock WHERE stock_id = %s', stock_id)
        result = cur.fetchone()
        if not result:
            stock = Stock("none", "none")
        else:
            stock = Stock(result[1], result[2])
            stock.set_stock_id(result[0])
            stock.set_creation_date(result[3])
            stock.set_last_edit(result[4])
        conn.close()
        return stock
    
    @staticmethod
    def get_stocks(username):
        conn = mysqlconnect()
        cur = conn.cursor()
        cur.execute('SELECT s.* FROM stockownership AS o JOIN stock AS s ON o.stock_id = s.stock_id WHERE o.username = %s', username)
        result = cur.fetchall()
        conn.close()
        return result

    @staticmethod
    def get_stocks_filter(username, filter):
        conn = mysqlconnect()
        cur = conn.cursor()
        cur.execute("SELECT s.* FROM stockownership AS o JOIN stock AS s ON o.stock_id = s.stock_id WHERE o.username = %s and s.name LIKE %s", (username, "%" + filter + "%"))
        result = cur.fetchall()
        conn.close()
        return result

    def update_stock_name(self):
        conn = mysqlconnect()
        cur = conn.cursor()

        cur.execute('''UPDATE stock 
                       SET name = %s , last_edit= %s
                       WHERE stock_id = %s
                    ''', (self.__name,self.__last_edit,self.__stock_id))
        conn.commit()
        print('stock name updated')
        
        conn.close()

    def update_stock_description(self):
        conn = mysqlconnect()
        cur = conn.cursor()

        cur.execute('''UPDATE stock 
                       SET description = %s, last_edit= %s
                       WHERE stock_id = %s
                    ''', (self.__description,self.__last_edit,self.__stock_id))
        conn.commit()
        print('stock description updated')
        
        conn.close()

    @staticmethod
    def delete_stock(stock_id):
        conn = mysqlconnect()
        cur = conn.cursor()
        cur.execute('DELETE FROM stock WHERE stock_id = %s', stock_id)
        conn.commit()
        print('stock deleted')
        conn.close()



    