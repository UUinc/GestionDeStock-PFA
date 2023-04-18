from connect import *

class Product:
    __product_id = -1

    def __init__(self, name, description, unit_price, quantity, alert_threshold, last_entry_date, last_release_date):
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

    def set_product_id(self, id):
        self.__product_id = id

    def set_product(self, name, description, unit_price, quantity, alert_threshold, last_entry_date, last_release_date):
        self.__name = name
        self.__description = description
        self.__unit_price = unit_price
        self.__quantity = quantity
        self.__alert_threshold = alert_threshold
        self.__last_entry_date = last_entry_date
        self.__last_release_date = last_release_date

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


# p1 = Product('9oo9a', 'fakiha mofida', 20, 10, 2, '2023-10-20', '2023-10-25')
# p1.add_product(1)
# p1.set_product('9oo9a', 'fakiha mofida jidan', 25, 15, 2, '2023-10-20', '2023-10-25')
# p1.update_product(1)
# print(p1)
