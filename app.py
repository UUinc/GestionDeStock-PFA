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
    try:
        cur.execute('INSERT INTO user VALUES(%s, %s, %s, %s, %s)', addUser())
        conn.commit()
        print('new user added')
    except Exception as e:
        match e.args[1].split()[5].strip('\''):
            case 'PRIMARY':
                print("Username already exist")
            case 'UC_email':
                print("Email already exist")
    

    #Delete User
    username = input("username to delete: ")
    cur.execute('DELETE FROM user WHERE username = %s', username)
    conn.commit()
    print('user has been deleted')

    #Update User
    username, first, last, email, password = addUser()
    cur.execute('UPDATE user SET first_name = %s, last_name = %s, email = %s, password = %s WHERE username = %s', (first, last, email, password, username))
    conn.commit()
    print('user has been updated')

    #User list
    cur.execute("select * from user")
    output=cur.fetchall()
    for i in output:
        print(i)

    conn.close()

#main
if __name__ == "__main__":
    mysqlconnect()