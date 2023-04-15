import pymysql
import config

def addUser():
    print("Sign up")
    username = input("username: ")
    first_name = input("first name: ")
    last_name = input("last name: ")
    email = input("email: ")
    password = input("password: ")
    return (username, first_name, last_name, email, password)

def mysqlconnect():
    conn = pymysql.connect(
        host=config.HOST,
        user=config.USER,
        password=config.PASSWORD,
        db=config.DATABASE,
    )

    cur = conn.cursor()

    #Add User
    cur.execute('INSERT INTO user VALUES(%s, %s, %s, %s, %s)', addUser())
    conn.commit()
    print('new user added')

    #Delete User
    username = input("username to delete: ")
    cur.execute('DELETE FROM user WHERE username = %s', username)
    conn.commit()
    print('user has been deleted')


    #User list
    cur.execute("select * from user")
    output=cur.fetchall()
    for i in output:
        print(i)

    conn.close()


#main
if __name__ == "__main__":
    mysqlconnect()