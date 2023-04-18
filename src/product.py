from connect import *

class Product:
    product_id = -1
    def __init__(self, name, description, unit_price, quantity, alert_threshold, last_entry_date, last_release_date):
        set_product(self, name, description, unit_price, quantity, alert_threshold, last_entry_date, last_release_date)
    
    def __str__(self):
        product = f"Product ({self.product_id})\n"
        product += f" name: ({self.name})\n"
        product += f" description: ({self.description})\n"
        product += f" unit price: ({self.unit_price})\n"
        product += f" quantity: ({self.quantity})\n"
        product += f" alert threshold: ({self.alert_threshold})\n"
        product += f" last entry date: ({self.last_entry_date})\n"
        product += f" last release date: ({self.last_release_date})\n"
        return product

    def set_product_id(self, id):
        self.product_id = id

    def set_product(self, name, description, unit_price, quantity, alert_threshold, last_entry_date, last_release_date):
        self.name = name
        self.description = description
        self.unit_price = unit_price
        self.quantity = quantity
        self.alert_threshold = alert_threshold
        self.last_entry_date = last_entry_date
        self.last_release_date = last_release_date

    def add_product(self):
        conn = mysqlconnect()
        cur = conn.cursor()

        cur.execute('''INSERT INTO product(name, description, unit_price, quantity, alert_threshold, last_entry_date, last_release_date, stock_id) 
                       VALUES(%s, %s, %s, %s, %s, %s, %s, %s)''', 
                    (self.name, self.description, self.unit_price, self.quantity, self.alert_threshold, self.last_entry_date, self.last_release_date, stock_id))
        conn.commit()
        print('new product added')
        
        conn.close()

    def delete_product(self):
        conn = mysqlconnect()
        cur = conn.cursor()

        cur.execute('DELETE FROM product WHERE product_id = %s', self.product_id)
        conn.commit()
        print('product deleted')
        
        conn.close()
    
    def update_product(self):
        conn = mysqlconnect()
        cur = conn.cursor()

        cur.execute('''UPDATE product 
                       SET name = %s, description = %s, unit_price = %s, quantity = %s, alert_threshold = %s, last_entry_date = %s, last_release_date = %s, stock_id = %s 
                       WHERE product_id = %s
                    ''', (self.name, self.description, self.unit_price, self.quantity, self.alert_threshold, self.last_entry_date, self.last_release_date, stock_id, self.product_id))
        conn.commit()
        print('product updated')
        
        conn.close()
