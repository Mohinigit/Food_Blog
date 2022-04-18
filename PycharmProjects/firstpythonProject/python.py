import pymysql
db_connection = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "Mohi@123",
    database = "college"
)

db_cursor = db_connection.cursor()
db_cursor.execute("CREATE DATABASE College")
db_cursor.execute("SHOW DATABASES")
for db in db_cursor:
    print(db)

db_cursor.execute("CREATE TABLE student (id INT , name VARCHAR(50) , course VARCHAR(50) , city VARCHAR(50))")
db_cursor.execute("SHOW TABLES")
for table in db_cursor:
   print(table)

db_cursor.execute("ALTER TABLE student MODIFY id INT PRIMARY KEY")
db_cursor.execute("INSERT INTO student (id , name , course , city) VALUES (01 , 'Sakshi' , 'Python' , 'Nagpur')")
db_cursor.execute("INSERT INTO student (id , name , course , city) VALUES (02 , 'Sarth' , 'Python' , 'Raipur')")
db_cursor.execute("INSERT INTO student (id , name , course , city) VALUES (03 , 'Kriti' , 'Php' , 'Jabalpur')")
db_cursor.execute("INSERT INTO student (id , name , course , city) VALUES (04 , 'Ankita' , 'Java' , 'Nagpur')")


db_cursor.execute("CREATE TABLE student_detail (id INT  , course VARCHAR(50) , duration VARCHAR(50))")
db_cursor.execute("ALTER TABLE student_detail ADD CONSTRAINT FK_student_det FOREIGN KEY (id) REFERENCES student(id)")
db_cursor.execute("INSERT INTO student_detail (id , course , duration) VALUES (01 , 'Python' , '3mons')")
db_cursor.execute("INSERT INTO student_detail (id , course , duration) VALUES (02 , 'Python' , '3mons')")
db_cursor.execute("INSERT INTO student_detail (id , course , duration) VALUES (03 , 'Php' , '4mons')")
db_cursor.execute("INSERT INTO student_detail (id , course , duration) VALUES (04 , 'Java' , '2mons')")


db_connection.commit()
print(db_cursor.rowcount , "Record Inserted")
