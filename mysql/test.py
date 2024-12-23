import mysql.connector

mydb = mysql.connector.connect(
    host='localhost', 
    user='root', 
    password='zoya@123'
)

print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
# mydb.commit()
# mydb.close()

for x in mycursor:
    print(x)
