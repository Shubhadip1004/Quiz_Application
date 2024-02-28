import sys
import mysql.connector
import login
import quiz
import question_submission
import current_best



def connection_to_database():
    try:
        connect = mysql.connector.connect(
            host = "localhost", 
            user = "root", 
            passwd = "root", 
            database = "quiz_application")
        
        
        if connect.is_connected():
            print()
            print("Connection is Secure and Successful !!!")
            global cursor
            cursor = connect.cursor()
            
        else:
            print("Failed to Connect to MySQL Database !!!")
    except mysql.connector.error as e:
        print(f"Error Connecting to the MySQL Database ::: {e}")


def user_driver():
    (username, flag) = login.user_login()
    if flag:
        print('''
        1. Attempt Quiz
        2. Submit Question
        3. Show Current Best Score
        4. Exit
        Press any other Integer to go to Main Menu
        ''')
            
        option = int(input("Enter Your Choice ::: "))
        if option == 1:
            quiz.contest(username)
            user_driver()
        elif option == 2:
            question_submission.submission()
            user_driver()
        elif option == 3:
            current_best.show(username)
            user_driver()
        elif option == 4:
            sys.exit()
        else:
            import main
            main.driver()
    else:
        print("Signing Off ... ")
        sys.exit()

# _ _ driver code _ _
# user_driver()