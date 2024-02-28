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
        
        global cur
        cur = connect.cursor()
        
        if connect.is_connected():
            print()
            print("Connection is Secure and Successful !!!")
            
        else:
            print("Failed to Connect to MySQL Database !!!")
    except mysql.connector.error as e:
        print(f"Error Connecting to the MySQL Database ::: {e}")

def user_login():
    connection_to_database()
    user_name = input("Enter the Username ::: ")
    pass_code = input("Enter the Passcode ::: ")
    query = "Select * from users"
    cur.execute(query)
    records = cur.fetchall()
    if (user_name,pass_code) in records:
        print("Access Granted !!! ")
        return user_name
    else:
        print("Access Denied !!!")
        print(f"No user '{user_name}' is found !!!")
    
    

def admin_login():
    connection_to_database()
    user_name = input("Enter the Username ::: ")
    pass_code = input("Enter the Passcode ::: ")
    
    if user_name == "admin" and pass_code == "admin":
        print("Authentication Successful !!!")
        print("Welcome Admin !!!")
    else:
        print("Access Denied !!! ")
        sys.exit()
