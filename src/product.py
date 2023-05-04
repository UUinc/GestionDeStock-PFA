from src.connect import *
from src.utils import *

class Product:
    __product_id = -1

    def __init__(self, name='', description='', unit_price=0, quantity=0, alert_threshold=0, last_entry_date='', last_release_date=''):
        self.__name = name
        self.__description = description
        self.__unit_price = unit_price
        self.__quantity = quantity
        self.__alert_threshold = alert_threshold
        self.__last_entry_date = last_entry_date
        self.__last_release_date = last_release_date
    
    def __str__(self):
        product = f"Product ({self.__product_id})\n"
        product += f" name: ({self.__name})\n"
        product += f" description: ({self.__description})\n"
        product += f" unit price: ({self.__unit_price})\n"
        product += f" quantity: ({self.__quantity})\n"
        product += f" alert threshold: ({self.__alert_threshold})\n"
        product += f" last entry date: ({self.__last_entry_date})\n"
        product += f" last release date: ({self.__last_release_date})\n"
        return product

    #Setters    
    def set_product_id(self, id):
        self.__product_id = id

    def set_name(self, name):
        self.__name = name

    def set_description(self, description):
        self.__description = description

    def set_alert_threshold(self, alert_threshold):
        self.__alert_threshold = alert_threshold

    def set_unit_price(self, unit_price):
        self.__unit_price = unit_price

    def add_quantity(self, value):
        self.__quantity += value
        self.__last_entry_date = current_timestamp()

    def remove_quantity(self, value):
        if value > self.__quantity:
            print('Error: Cannot remove quantity. The requested value is higher than the current quantity in stock. Please enter a lower value or check the current stock level before proceeding.')
            return
        self.__quantity -= value
        self.__last_release_date = current_timestamp()

    #CRUD
    @staticmethod
    def get_product(product_id):
        conn = mysqlconnect()
        cur = conn.cursor()
        cur.execute('SELECT * FROM product WHERE product_id = %s', product_id)
        result = cur.fetchone()
        product = Product(result[1], result[2], result[3], result[4], result[5], result[6], result[7])
        product.set_product_id(result[0])
        conn.close()
        return product
    
    @staticmethod
    def get_products(stock_id):
        conn = mysqlconnect()
        cur = conn.cursor()
        cur.execute('SELECT * FROM product WHERE stock_id = %s', stock_id)
        result = cur.fetchall()
        conn.close()
        return result

    def add_product(self, stock_id):
        conn = mysqlconnect()
        cur = conn.cursor()
        cur.execute('''INSERT INTO product(name, description, unit_price, quantity, alert_threshold, last_entry_date, last_release_date, stock_id) 
                       VALUES(%s, %s, %s, %s, %s, %s, %s, %s)''', 
                    (self.__name, self.__description, self.__unit_price, self.__quantity, self.__alert_threshold, self.__last_entry_date, self.__last_release_date, stock_id))
        conn.commit()
        self.__product_id = cur.lastrowid
        print('new product added')
        conn.close()

    def delete_product(self):
        conn = mysqlconnect()
        cur = conn.cursor()
        cur.execute('DELETE FROM product WHERE product_id = %s', self.__product_id)
        conn.commit()
        print('product deleted')
        conn.close()
    
    def update_product(self, stock_id):
        conn = mysqlconnect()
        cur = conn.cursor()
        cur.execute('''UPDATE product 
                       SET name = %s, description = %s, unit_price = %s, quantity = %s, alert_threshold = %s, last_entry_date = %s, last_release_date = %s, stock_id = %s 
                       WHERE product_id = %s
                    ''', (self.__name, self.__description, self.__unit_price, self.__quantity, self.__alert_threshold, self.__last_entry_date, self.__last_release_date, stock_id, self.__product_id))
        conn.commit()
        print('product updated')
        
        conn.close()
