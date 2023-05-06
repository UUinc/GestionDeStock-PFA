# STOCK.ME 📦

This is a desktop application developed using Python\'s tkinter library
and MySQL for managing inventory. This application is designed to
provide an easy-to-use interface for managing stock and inventory of
products in a small to medium-sized business.

## Features

-   User authentication with a secure login system.
-   Secure User Registration with Username, Email, and Password Validation.
-   User settings page to modify user information.
-   Create, update, and delete stocks with detailed stock information
    such as stock name, description, and owners.
-   Add, update, and delete products with detailed product information
    such as product name, description, price, quantity, and alert threshold.
-   Display a list of all products with their respective details in a
    table format.
-   Search and filter products based on product name.
-   Notification page to reports for low stock or out of stock products.
-   Manage multiple users with different levels of access.
-   Easy to use and intuitive interface.

## Installation

To install this application on your computer, follow the below steps:

1.  Download the source code from the GitHub repository: https://github.com/UUinc/stock.me
2.  Install Python 3.10 or higher version from
<a href="https://www.python.org/downloads/" target="_new">https://www.python.org/downloads/</a>
3.  Install the following Python packages: __ttkbootstrap__, __pymysql__.

```
pip install ttkbootstrap pymysql
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

6.  Run the `app.py` file to start the application.

```
python app.py
```

#### ⚠️ To enhance your app experience, it is recommended to use a resolution of 1920x1080 for optimal display.

## Usage

Once you run the application, the login screen will appear. Enter your
credentials to access the main screen. From there, you can navigate to
different screens to perform the desired action.

## Demo

![image](https://user-images.githubusercontent.com/63449913/236636369-6c9cda33-9758-4b5b-bde9-d6259f831b4b.png)
![image](https://user-images.githubusercontent.com/63449913/236636325-e4d69f6e-5b76-4ec2-8940-317c07dc3026.png)
![image](https://user-images.githubusercontent.com/63449913/236636159-d89bd6a1-ed1d-4e1d-b845-669495cfa2e6.png)
![image](https://user-images.githubusercontent.com/63449913/236636201-935a5862-f88d-4a87-afdc-94624850b989.png)
![image](https://user-images.githubusercontent.com/63449913/236636247-c0c7474b-f5cd-4e18-bc2b-3c041e0c9a80.png)
![image](https://user-images.githubusercontent.com/63449913/236636462-297575c9-80a4-40c2-95ad-82b770bf2f81.png)
![image](https://user-images.githubusercontent.com/63449913/236636520-04b966d7-3daa-48cd-a28f-d7dd9b7b7208.png)
![image](https://user-images.githubusercontent.com/63449913/236636592-90831e1d-70b0-46b3-af25-a579fe8d0406.png)

## Credits

This project was developed by <a href="https://github.com/UUinc" target="_blank">Yahya Lazrek</a>, <a href="https://github.com/yousraeb" target="_blank">Yousra Elbarraq</a> and <a href="https://github.com/OuassimaAboukhair" target="_blank">Ouassima Aboukhair</a> under the guidance of Dr. Mohammed Ameksa. We would like to thank our project guide for his valuable support and guidance throughout the project.
                      
#### if you have any question feel free to ask :smile:

### Contacts

-   uu.soft.inc@gmail.com
-   [twitter](https://twitter.com/yahya_lz)
-   [github](https://github.com/UUinc)
