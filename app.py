import pymysql
import config

def mysqlconnect():
    conn = pymysql.connect(
        host=config.HOST,
        user=config.USER,
        password=config.PASSWORD,
        db=config.DATABASE,
    )

    cur = conn.cursor()

    #select query
    cur.execute("select * from user")
    output=cur.fetchall()

    for i in output:
        print(i)

    conn.close()


#main
if __name__ == "__main__":
    mysqlconnect()