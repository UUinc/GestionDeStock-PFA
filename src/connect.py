import pymysql
import config

def mysqlconnect():
    conn = pymysql.connect(
        host=config.HOST,
        user=config.USER,
        password=config.PASSWORD,
        db=config.DATABASE,
    )

    return conn