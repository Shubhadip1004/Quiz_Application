create database quiz_application;
use quiz_application;

create table users(
username varchar(35) Primary Key,
passcode varchar(20) not null
);

create table scorecard(
date_and_time datetime ,
username varchar(35) ,
score integer not null ,
primary key(date_and_time, username)
);

create table questions(
question_id integer Primary Key,
question varchar(100) not null,
option1 varchar(30) not null,
option2 varchar(30) not null,
option3 varchar(30) not null,
option4 varchar(30) not null,
answer varchar(30) not null
);

create table admin_questions(
question_id integer Primary Key,
question varchar(100) not null,
option1 varchar(30) not null,
option2 varchar(30) not null,
option3 varchar(30) not null,
option4 varchar(30) not null,
answer varchar(30) not null
);

insert into questions(question_id, question, option1, option2, option3, option4, answer)
values 
(1, "What is the capital city of Australia?","Sydney", "Melbourne", "Canberra", "Perth", "Canberra"),
(2, "Who wrote the novel 'To kill a Mockingbird'?", "Harper Lee", "J.K.Rowling", "Ernest Hemmingway", "Mark Twain", "Harper Lee"),
(3, "Which planet is known as Red Planet?", "Earth","Jupyter", "Mars", "Venus", "Mars"),
(4, "Which of the following is a prime number?", "17", "20", "1", "34", "17"),
(5, "Who painted Monalisa?", "Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Michelangelo", "Leonardo da Vinci"),
(6, "What is the chemical symbol of water?","H2O", "CO2", "HCl", "CH4", "H2O"),
(7, "In which year did World War 1 begin?", "1905", "1914", "1922", "1939", "1914"),
(8, "Who is known as the Father of Modern Physics?", "Issac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla", "Albert Einstein"),
(9, "What is the tallest mountain in the world?", "Mount Kilimanjaro", "Mount Everest", "Mount Fuji", "K2", "Mount Everest"),
(10, "Who wrote the play 'Romeo and Juliet'?", "William Shakespeare", "George Bernard Shaw", "Tennessee Williams", "Arthur Miller", "William Shakespeare"),
(11, "What is the chemical symbol for gold?", "Au", "Ag", "Cu", "Fe", "Au"),
(12, "Who was the first woman to fly solo across the Atlantic Ocean?", "Amelia Earhart", "Bessie Coleman", "Harriet Quimby", "Sally Ride", "Amelia Earhart"),
(13, "Which gas is most abundant in Earth's atmosphere?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Argon", "Nitrogen"),
(14, "What is the chemical symbol for silver?", "Si", "Ag", "Sr", "Sn", "Ag"),
(15, "Who wrote the famous novel '1984'?", "George Orwell", "Aldous Huxley", "Franz Kafka", "Ray Bradbury", "George Orwell"),
(16, "Which country is known as the Land of the Rising Sun?", "China", "South Korea", "Japan", "Vietnam", "Japan"),
(17, "What is the largest organ in the human body?", "Liver", "Brain", "Skin", "Heart", "Skin"),
(18, "Who discovered Penicillin?", "Louis Pasteur", "Jonas Salk", "Marie Curie", "Alexander Fleming", "Alexander Fleming"),
(19, "What is the chemical symbol for Iron?", "Ir", "Fe", "In", "I", "Fe"),
(20, "Who was the first person to step on the moon?", "Buzz Aldrin", "Yuri Gararin", "Michael Collins", "Neil Armstrong", "Neil Armstrong")
;

