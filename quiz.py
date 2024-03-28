import random
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

def access_scorecard(username, new_score):
    connection_to_database()
    query = "Select * from scorecard"
    cur.execute(query)
    
    records = cur.fetchall()
    for record in records:
        if username in record: # if user has already been on scorecard
            command = "Select score from scorecard where username = %s"
            cur.execute(command, (username,))
            score = (cur.fetchone())[0]
            if new_score > score: 
                sql = "Update scorecard Set score = %s Where username = %s"
                val = (new_score, username)
                cur.execute(sql,val)
                connect.commit()
            return None
    
    add_query = "insert into scorecard(username, score) values(%s, %s)"
    cur.execute(add_query, (username, new_score))
    connect.commit()
    return None
    
    
    

def contest(username):
    connection_to_database()
    query = "Select * from questions"
    cur.execute(query)
    
    ques_set = cur.fetchall()
    
    sql = "Select Count(*) from questions"
    cur.execute(sql)
    
    count_question = (cur.fetchone())[0]
    
    random_ques_no_set = []
    while len(random_ques_no_set) != 10:
        x = random.randint(1,count_question)
        if x in random_ques_no_set:
            continue
        random_ques_no_set.append(x)
    # random_ques_no_set = np.random.randint(1,count_question+1, 11)
    
    questions, op1s, op2s, op3s, op4s, anss = [], [], [], [] ,[] ,[]
    
    for i in ques_set:
        (no, question, op1, op2, op3, op4, ans) = i
        if no not in random_ques_no_set:
            pass
        else:
            questions.append(question)
            op1s.append(op1)
            op2s.append(op2)
            op3s.append(op3)
            op4s.append(op4)
            anss.append(ans)
    
    # print("Random Question Set Number ::: ",random_ques_no_set)
    # print("Question ::: ",questions)
    # print("Option 1 ::: ",op1s)
    # print("Option 2 ::: ",op2s)
    # print("Option 3 ::: ",op3s)
    # print("Option 4 ::: ",op4s)
    # print("Answers  ::: ",anss)
    
    
    init_score = 0
    flag = True
    
    while flag and init_score < 10:
        print(" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
        print(f"Question {init_score + 1}: {questions[init_score]}")
        print(f"Option 1: {op1s[init_score]}")
        print(f"Option 2: {op2s[init_score]}")
        print(f"Option 3: {op3s[init_score]}")
        print(f"Option 4: {op4s[init_score]}")
        print()
        val = int(input("Enter Answer ::: "))
        print()
        if val == 1:
            if anss[init_score] == op1s[init_score]:
                init_score = init_score + 1
            else:
                flag = False
                access_scorecard(username, init_score)
        elif val == 2:
            if anss[init_score] == op2s[init_score]:
                init_score = init_score + 1
            else:
                flag = False
                access_scorecard(username, init_score)
        elif val == 3:
            if anss[init_score] == op3s[init_score]:
                init_score = init_score + 1
            else:
                flag = False
                access_scorecard(username, init_score)
        elif val == 4:
            if anss[init_score] == op4s[init_score]:
                init_score = init_score + 1
            else:
                flag = False
                access_scorecard(username, init_score)
        else:
            print("Invalid Input !!!")
            print("Signing Out ...")
            access_scorecard(username, init_score)
    
    if init_score == 10:
        print("Congratulations !!!")
        print(f"Great Job {username} !!!")
        access_scorecard(username, init_score)
        
    print(f"Your Score is {init_score}")
    return None

# _ _ driver code _ _
# contest("user")
