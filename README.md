# Gestion de stock Desktop Application

This is a desktop application developed using Python\'s tkinter library
and MySQL for managing inventory. This application is designed to
provide an easy-to-use interface for managing stock and inventory of
products in a small to medium-sized business.

## Features

-   User authentication with a secure login system.
-   Add, update, and delete products with detailed product information
    such as product name, description, price, quantity, and category.
-   Display a list of all products with their respective details in a
    table format.
-   Search and filter products based on category or name.
-   Create, edit, and delete product categories.
-   Generate reports for product stock, sales, and revenue.
-   Manage multiple users with different levels of access.
-   Easy to use and intuitive interface.

## Installation

To install this application on your computer, follow the below steps:

1.  Download the source code from the GitHub repository: https://github.com/UUinc/GestionDeStock-PFA
2.  Install Python 3.10 or higher version from
<a href="https://www.python.org/downloads/" target="_new">https://www.python.org/downloads/</a>
3.  Install the following Python packages: tkinter,
    pymysql. You can install them using pip or conda
    package managers. For example, in pip, you can run the following
    command:

```
pip install tkinter pymysql
```

4.  Create a MySQL database, and import the `database.sql` file from the
    source code to set up the required tables and data.
5.  Edit the `config.py` file with your MySQL database details such as
    username, password, host, and database name.

```
# MySQL Database Configuration
HOST = "localhost"
USER = "root"
PASSWORD = "password"
DATABASE = "gestion_stock"
```

6.  Run the `main.py` file to start the application.

## Usage

Once you run the application, the login screen will appear. Enter your
credentials to access the main screen. From there, you can navigate to
different screens to perform the desired action.

## Demo

website: http://uuinc.github.io/gestion-de-stock-pfa-web

![Dairy_Inventory_Web_App](https://user-images.githubusercontent.com/63449913/229149190-6f7b5db5-05f6-4c87-b94f-3943a900bec7.png)

## Credits

This project was developed by Yahya Lazrek, Yousra Elbarraq and Ouassima Aboukhair under the guidance of Dr. Mohammed Ameksa. We would like to thank our project guide for his valuable support and guidance throughout the project.
                      
#### if you have any question feel free to ask :smile:

### Contacts

-   uu.soft.inc@gmail.com
-   [twitter](https://twitter.com/yahya_lz)
-   [github](https://github.com/UUinc)
