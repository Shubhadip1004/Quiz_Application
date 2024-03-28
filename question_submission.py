import sys
import time
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
            # print("Connection is Secure and Successful !!!")
            global cur
            cur = connect.cursor()
            
        else:
            print("Failed to Connect to MySQL Database !!!")
    except mysql.connector.error as e:
        print(f"Error Connecting to the MySQL Database ::: {e}")

def submission():
    connection_to_database()
    print('''
Points To be Considered :::

1. The Question should be MCQ type.
2. The no. of characters allowed in the Question is at max 100 and at least 1.
3. The no. of characters allowed in the Option Section is at max 35 and at least 1.
4. All the Questions will be submitted to Admin before acceptance.
5. Check for Redundancy in Question Submission.
6. Please provide the Answer same as in the Option.
          
    ''')
    question = input("Enter the Question ::: ")
    option1 = input("Enter Option 1 ::: ")
    option2 = input("Enter Option 2 ::: ")
    option3 = input("Enter Option 3 ::: ")
    option4 = input("Enter Option 4 ::: ")
    answer = input("Enter Correct Answer ::: ")
    
    if answer not in [option1, option2, option3, option4]:
        time.sleep(0.5)
        print("Error Detecting !!!")
        time.sleep(1.5)
        print("Answer is NOT matching with ANY Options !!!")
        return None
    
    sql = "Select Count(*) from admin_questions"
    cur.execute(sql)
    count_question = (cur.fetchone())[0]
    question_no = count_question + 1
    
    add_query = "insert into admin_questions(question_id,question,option1,option2,option3,option4, answer) values(%s, %s, %s, %s, %s, %s, %s)"
    val = (question_no,question,option1,option2,option3,option4,answer)
    cur.execute(add_query, val)
    connect.commit()
    return None
    
# _ _ driver code _ _
# submission()