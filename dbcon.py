import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host = "localhost",
        database = "google",
        user = "root",
        password = "Diya@289"
    )
    
    if connection.is_connected():
        pass

except Error as e:
    print("mysql connection error",e)    