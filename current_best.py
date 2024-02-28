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

def show(username):
    connection_to_database()
    query = "select score from scorecard where username = %s"
    cur.execute(query,(username,))
    score = cur.fetchone()
    
    if score:
        print(f"Highest score by {username} is ::: {score[0]}")
    else:
        print(f"No user named '{username}' is found !!!")
    
    return None