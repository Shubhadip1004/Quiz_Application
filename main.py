import sys
import time
import mysql.connector
import login
import register

# db_username = input("Enter the User for connecting to Database ::: ")
# db_password = input("Enter the password  for connecting to Database ::: ")
db_username = 'root'
db_password = 'root'


def connection_to_database():
    try:
        connect = mysql.connector.connect(
            host = "localhost", 
            user = db_username, 
            passwd = db_password, 
            database = "quiz_application")
        
        loading_screen()
        if connect.is_connected():
            
            print()
            print("Connection is Secure and Successful !!!")
            global cursor
            cursor = connect.cursor()
            
        else:
            print("Failed to Connect to MySQL Database !!!")
    except mysql.connector.error as e:
        print(f"Error Connecting to the MySQL Database ::: {e}")


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

def driver():
    connection_to_database()
    print('''
          Press 1 for Admin
          Press 2 for User
          Press 3 to Register
          Press 4 to Quit
          ''')
    choice = int(input("Enter Choice ::: "))
    if choice == 1:
        import admin
        admin.admin_driver()
    elif choice == 2:
        import user
        user.user_driver()
    elif choice == 3:
        register.new_user()
        driver()
    elif choice == 4:
        sys.exit()
    else:
        print("Invalid Input")
        driver()

# _ _ driver code _ _
driver()