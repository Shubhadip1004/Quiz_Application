import sys
import mysql.connector
import login
import analysis
import question_acceptance

def connection_to_database():
    try:
        connect = mysql.connector.connect(
            host = "localhost", 
            user = "root", 
            passwd = "root", 
            database = "quiz_application")
        
        
        if connect.is_connected():
            print()
            # print("Connection is Secure and Successful !!!")
            global cursor
            cursor = connect.cursor()
            
        else:
            print("Failed to Connect to MySQL Database !!!")
    except mysql.connector.error as e:
        print(f"Error Connecting to the MySQL Database ::: {e}")

def admin_driver():
    flag = login.admin_login()
    def admin_main():
        print('''
        1. Analysis
        2. Question Acceptance
        3. Exit
        Press any other Integer to go to Main Menu
        ''')
            
        option = int(input("Enter Your Choice ::: "))
        if option == 1:
            analysis.analysis_driver(flagger = True)
            admin_driver()
        elif option == 2:
            question_acceptance.acceptance()
            admin_driver()
        elif option == 3:
            sys.exit()
        else:
            import main
            # main.driver()
    if flag:
        admin_main()
    else:
        print("Signing Off ... ")
        sys.exit()
        
# _ _ driver _ _
# admin_driver()