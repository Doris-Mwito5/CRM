import mysql.connector

#create db connection
database = mysql.connector.connect(
    host ='localhost',
    user ='root',
    passwd ='@Kawira123',
    
)

#create a cursor object
cursorobject = database.cursor()

#create a database
cursorobject.execute("CREATE DATABASE elderco")

print("All done")