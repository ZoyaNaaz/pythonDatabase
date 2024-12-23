import mysql.connector

mydb = mysql.connector.connect(
    host='localhost', 
    user='root', 
    password='zoya@123'
)

mycursor = mydb.cursor()
mycursor.execute("INSERT INTO test1.test_table VAlUES(1, 'zoya', 100, 9.4, 'meerut')")
mycursor.execute("INSERT INTO test1.test_table VAlUES(1, 'zoya', 100, 9.4, 'meerut')")
mycursor.execute("INSERT INTO test1.test_table VAlUES(1, 'zoya', 100, 9.4, 'meerut')")
mycursor.execute("INSERT INTO test1.test_table VAlUES(1, 'zoya', 100, 9.4, 'meerut')")
mycursor.execute("INSERT INTO test1.test_table VAlUES(1, 'zoya', 100, 9.4, 'meerut')")
mycursor.execute("INSERT INTO test1.test_table VAlUES(1, 'zoya', 100, 9.4, 'meerut')")
mycursor.execute("INSERT INTO test1.test_table VAlUES(1, 'zoya', 100, 9.4, 'meerut')")
mycursor.execute("INSERT INTO test1.test_table VAlUES(1, 'zoya', 100, 9.4, 'meerut')")
mycursor.execute("INSERT INTO test1.test_table VAlUES(1, 'zoya', 100, 9.4, 'meerut')")
mycursor.execute("INSERT INTO test1.test_table VAlUES(1, 'zoya', 100, 9.4, 'meerut')")
mydb.commit()
mydb.close()
