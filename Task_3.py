import mysql.connector

# Take credentials as input
host = input("Enter host name: ")
user = input("Enter user name: ")
password = input("Enter password: ")
database = input("Enter database name: ")
   
# Connect to MySQL   
db_conn = mysql.connector.connect(
   host = host,
   user = user,
   password = password,
   database = database
)
   
mycursor = db_conn.cursor()

# Create students table
mycursor.execute("""
   CREATE TABLE students  
   (
     id INT AUTO_INCREMENT PRIMARY KEY,   
     first_name VARCHAR(50),
     last_name VARCHAR(50),
     age INT,
     grade DECIMAL(5,2)
   )
""")

# Insert a new student record
sql = "INSERT INTO students (first_name, last_name, age, grade) VALUES (%s, %s, %s, %s)"
values = ("Alice", "Smith", 18, 95.5)
mycursor.execute(sql, values)

# Update grade of Alice to 97  
sql = "UPDATE students SET grade = %s WHERE first_name = 'Alice'"   
val = (97.0,)
mycursor.execute(sql, val)

# Delete Smith record
sql = "DELETE FROM students WHERE last_name ='Smith'"
mycursor.execute(sql) 

# Display records  
mycursor.execute("SELECT * FROM students") 
result = mycursor.fetchall()
for x in result:
   print(x) 

db_conn.commit()
mycursor.close()  
db_conn.close()
