from connect import *
from utils import *

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

    def set_description(self,description):
        self.__description = description

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

    #renaming
    def rename_stock(self,name):
        self.__name=name

    #deleting
    def delete_stock(self):
        conn = mysqlconnect()
        cur = conn.cursor()
        cur.execute('DELETE FROM stock WHERE stock_id = %s', self.__stock_id)
        conn.commit()
        print('stock deleted')
        conn.close()

stock = Stock('l3iba','eywaaaaaa')
print(stock)
stock.add_stock
    