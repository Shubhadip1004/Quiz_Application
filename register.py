import sys
import mysql.connector

def connection_to_database():
    try:
        global connect
        connect = mysql.connector.connect(
            host = "localhost", 
            user = "root", 
            passwd = "root", 
            database = "quiz_application")
        
        
        if connect.is_connected():
            print()
            print("Connection is Secure and Successful !!!")
            global cur
            cur = connect.cursor()
            
        else:
            print("Failed to Connect to MySQL Database !!!")
    except mysql.connector.error as e:
        print(f"Error Connecting to the MySQL Database ::: {e}")

def new_user():
    connection_to_database()
    new_username = input("Enter your Username ::: ")
    new_password = input("Enter password ::: ")
    confirm_password = input("Confirm password ::: ")
    
    if new_password != confirm_password:
        print("Password doesn't match the Confirm Password!!! ")
        sys.exit()
    
    query = "Select * from users"
    cur.execute(query)
    
    records = cur.fetchall()
    for record in records:
        if new_username in record:
            print(f"Username '{new_username}' is already taken !!!")
            sys.exit()
    
    add_query = "insert into users(username, passcode) values(%s, %s)"
    cur.execute(add_query, (new_username,new_password))
    connect.commit()
    
    print(f"New User '{new_username}' added to the database Successfully !!!")
            
    
# new_user()
