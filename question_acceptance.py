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

def acceptance():
    connection_to_database()
    
    counter = 0
    sql = "Select * from admin_questions"
    cur.execute(sql)
    submitted_questions = cur.fetchall()
    
    sql = "Select Count(*) from questions"
    cur.execute(sql)
    count_question = (cur.fetchone())[0]
    question_no = count_question + 1
    
    while counter < count_question:
        (x,question,option1,option2,option3,option4, answer) = submitted_questions[counter]
        print(" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
        print(f"Question {counter+1}: {question}")
        print(f"Option 1: {option1}")
        print(f"Option 2: {option2}")
        print(f"Option 3: {option3}")
        print(f"Option 4: {option4}")
        print(f"Answer  : {answer }")
        print()
        choice = input("Do you Want to Continue?(Yes/No) :::")
        if choice.lower() == 'no':
            return None
        else:
            val = int(input("To Add this Question, Enter 1 Else any Integer ::: "))
            print()
            if val == 1:
                add_query = "insert into questions(question_id,question,option1,option2,option3,option4, answer) values(%s, %s, %s, %s, %s, %s, %s)"
                val = (question_no,question,option1,option2,option3,option4,answer)
                cur.execute(add_query, val)
                connect.commit()
                question_no = question_no + 1


            # Deleting the top record
            sql = "Delete from admin_questions Where question_id = %s"
            val = x
            cur.execute(sql,(x,))
            connect.commit()
            
            # Decrementing the value of question_id
            sql = "Update admin_questions Set question_id = question_id - %s where question_id > 0"
            cur.execute(sql,(1,))
            connect.commit()
            counter = counter + 1
            
    return None
    
# _ _ driver code _ _
# acceptance()
    