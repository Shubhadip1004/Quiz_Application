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
            # print()
            # print("Connection is Secure and Successful !!!")
            global cur
            cur = connect.cursor()
            
        else:
            print("Failed to Connect to MySQL Database !!!")
    except mysql.connector.error as e:
        print(f"Error Connecting to the MySQL Database ::: {e}")

def show(table):
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
    if table == 'users':
        sql = "Select * from users"
        print()
        print("username || passcode")
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
    elif table == 'scorecard':
        sql = "Select * from scorecard"
        print()
        print("username || score")
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
    elif table == 'questions':
        sql = "Select * from questions"
        print()
        print("question_id || question || option 1 || option 2 || option 3 || option 4 || answer")
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
    elif table == 'admin_questions':
        sql = "Select * from admin_questions"
        print()
        print("question_id || question || option 1 || option 2 || option 3 || option 4 || answer")
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
    cur.execute(sql)
    records = cur.fetchall()
    for record in records:
        print(record)
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
    
    return None

def desc(table):
    
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
    if table == 'users':
        sql = "desc users"
        print()
        print("username || passcode")
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
    elif table == 'scorecard':
        sql = "desc scorecard"
        print()
        print("username || score")
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
    elif table == 'questions':
        sql = "desc questions"
        print()
        print("question_id || question || option 1 || option 2 || option 3 || option 4 || answer")
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
    elif table == 'admin_questions':
        sql = "desc admin_questions"
        print()
        print("question_id || question || option 1 || option 2 || option 3 || option 4 || answer")
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
    cur.execute(sql)
    records = cur.fetchall()
    for record in records:
        print(record)
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
    
    return None



def analysis_driver():
    def analysis_main():
        
            print('''

    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
                1. users table
                2. questions table
                3. admin_questions table
                4. scorecard table
                5. Exit
                Enter any other Integer to go to Main page
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
                ''')
            choice = int(input("Enter Your Choice ::: "))
            
            if choice == 1:
                print('''
                    1. Show Content
                    2. Description
                    3. Exit
                    Enter any integer to get Redirected to Analysis page
                    ''')
                option = int(input("Enter your Option ::: "))
                if option == 1:
                    show("users")
                elif option == 2:
                    desc("users")
                elif option == 3:
                    sys.exit()
                else:
                    analysis_driver()
                analysis_main()
            
            elif choice == 2:
                print('''
                    1. Show Content
                    2. Description
                    3. Exit
                    Enter any integer to get Redirected to Analysis page
                    ''')
                option = int(input("Enter your Option ::: "))
                if option == 1:
                    show("questions")
                elif option == 2:
                    desc("questions")
                elif option == 3:
                    sys.exit()
                else:
                    analysis_driver()
                analysis_main()
                    
            elif choice == 3:
                print('''
                    1. Show Content
                    2. Description
                    3. Exit
                    Enter any integer to get Redirected to Analysis page
                    ''')
                option = int(input("Enter your Option ::: "))
                if option == 1:
                    show("admin_questions")
                elif option == 2:
                    desc("admin_questions")
                elif option == 3:
                    sys.exit()
                else:
                    analysis_driver()
                analysis_main()
                
            elif choice == 4:
                print('''
                    1. Show Content
                    2. Description
                    3. Exit
                    Enter any integer to get Redirected to Analysis page
                    ''')
                option = int(input("Enter your Option ::: "))
                if option == 1:
                    show("scorecard")
                elif option == 2:
                    desc("scorecard")
                elif option == 3:
                    sys.exit()
                else:
                    analysis_driver()
                analysis_main()
                
            elif choice == 6:
                sys.exit() 
            
            else:
                import main
                sys.exit()
                
            
    connection_to_database()
    analysis_main()
        
# _ _ driver code _ _
# analysis_driver()