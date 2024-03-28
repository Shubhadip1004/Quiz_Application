# Quiz_Application
This is a Quiz Application developed using Python 3.10 and MySQL server.
<br> Author: @Shubhadip1004 (GitHub)

Description of Quiz Application:

<br>

1. Basic Idea:

<br>

~ Developing MySQL databases

~ Implement Login System and Register System

~ Code to Implement the Quiz App by connecting the MySQL server

<br>

<br>

2. Database Contents:

<br>

 i. question: It contains Question_ID, Question, Options(1 to 4) and the Answer
 
 ii. scoreboard: It contains Username(Primry Key) , Score_Achieved
 
 iii. admin: It will contain the Questions submitted by user. Upon Acceptance, the questions will be transfered from Admin to Questions database.
 
 iv. users: It Contains Username(Primary Key), Passcode

<br>

Initially, 20 questions will be present in the Questions Database among which randomly 15 will be asked.

<br>

3. Python Code:

<br>
   
 i. Connect the database
 
 ii. Create a authentication system to allow different operations for both admin and user
 
   ii.i. Separate login details by different users 
 
   ii.ii Register by the Approval of Admin
 
 iii. Create the Quiz System 
 
 iv. Questions can be added on the system by the user upon approval by admin

 
<br>
Database Schema:

<br>

 1. users{
    
	username: varchar(35) Primary Key

	passcode: varchar(35) Not Null

	}
 <br>
 
 2. scoreboard{

  	username: varchar(35) Primary Key
  
  	score: integer Not Null
 
  	}
 <br>
 
 3. questions{
    
	question_id: integer Primary Key

	question: varchar(100) Not Null

	option1: varchar(30) Not Null

	option2: varchar(30) Not Null

	option3: varchar(30) Not Null

	option4: varchar(30) Not Null

	answer: varchar(30) Not Null

	}
  <br>

 4. admin_questions {
    
       question_id: integer Primary Key

       question: varchar(100) Not Null

       option1: varchar(30) Not Null

       option2: varchar(30) Not Null

       option3: varchar(30) Not Null

       option4: varchar(30) Not Null

       answer: varchar(30) Not Null

       }
  
  <br>

<br>
How To Use:
<br>

1. Run the "quiz_application_query.sql" <br>
2. Check whether all the required modules (mysql.connector, sys, time, random) are present or not. <br>
3. Run the Main function <br>

<br>
<br>





