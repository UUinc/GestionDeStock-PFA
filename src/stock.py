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
    
    #setters
    def set_stock_id(self, id):
        self.__stock_id = id

    def set_name(self, name):
        self.__name = name
        self.__last_edit=current_timestamp()

    def set_description(self,description):
        self.__description = description
        self.__last_edit=current_timestamp()

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
        stock = Stock(result[1], result[2], result[3])
        stock.set_stock_id(result[0])
        conn.close()
        return stock

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

    def update_stock_description(self,description):
        conn = mysqlconnect()
        cur = conn.cursor()

        cur.execute('''UPDATE stock 
                       SET description = %s, last_edit= %s
                       WHERE stock_id = %s
                    ''', (self.__description,self.__last_edit,self.__stock_id))
        conn.commit()
        print('stock description updated')
        
        conn.close()

    def delete_stock(self):
        conn = mysqlconnect()
        cur = conn.cursor()
        cur.execute('DELETE FROM stock WHERE stock_id = %s', self.__stock_id)
        conn.commit()
        print('stock deleted')
        conn.close()



    