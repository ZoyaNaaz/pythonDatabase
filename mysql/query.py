import mysql.connector

mydb = mysql.connector.connect(
    host='localhost', 
    user='root', 
    password='zoya@123'
)

mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM test1.test_table")
mycursor.execute("SELECT c1, c5 FROM test1.test_table")
for i in mycursor.fetchall():
    print(i)

mydb.close()
