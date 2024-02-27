import time
import sys
import mysql.connector 

def loading_screen():
    for i in range(13):
        time.sleep(0.5)
        if i % 4 == 0:
            print(" |  Connecting... ")   
        elif i % 4 == 1:
            print(" /  Connecting... ")
        elif i % 4 == 2:
            print(" -  Connecting... ")
        elif i % 4 == 3:
            print(" \  Connecting... ")
    

def user_login():
    user_name = input("Enter the Username ::: ")
    pass_code = input("Enter the Passcode ::: ")
    query = "Select * from users"
    cursor.execute(query)
    records = cursor.fetchall()
    if (user_name,pass_code) in records:
        print("Access Granted !!! ")
    else:
        print("Access Denied !!!")
        print(f"No user '{user_name}' is found !!!")
    

def admin_login():
    user_name = input("Enter the Username ::: ")
    pass_code = input("Enter the Passcode ::: ")
    
    if user_name == "admin" and pass_code == "admin":
        print("Authentication Successful !!!")
        print("Welcome Admin !!!")
    else:
        print("Access Denied !!! ")
        sys.exit()

def login():
    print('''
          Press 1 for Admin
          Press 2 for User
          Press 3 to Quit
          ''')
    choice = int(input("Enter Choice ::: "))
    if choice == 1:
        admin_login()
    elif choice == 2:
        user_login()
    elif choice == 3:
        sys.exit()
    else:
        print("Invalid Input")
        login()

def connection_to_database():
    try:
        loading_screen()
        connection = mysql.connector.connect(
            host = "localhost", 
            user = "root", 
            passwd = "root", 
            database = "quiz_application")
        
        
        if connection.is_connected():
            print("Connection is Secure and Successful !!!")
            global cursor
            cursor = connection.cursor()
            login()
        else:
            print("Failed to Connect to MySQL Database !!!")
    except mysql.connector.error as e:
        print(f"Error Connecting to the MySQL Database ::: {e}")


# _ _ Driver Code _ _
connection_to_database()
