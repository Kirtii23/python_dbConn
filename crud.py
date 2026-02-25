from dbcon import connection

# TblCreateQuery = """
#      CREATE TABLE students(
#        id INT PRIMARY KEY AUTO_INCREMENT,
#        stdName VARCHAR(200),
#        stdCourses VARCHAR(100),
#        rollNo INT(20)
#        )
#        """

#cursor = connection.cursor()
#cursor.execute(TblCreateQuery)

#InsertData = """INSERT INTO students(stdName,stdCourses,rollno) VALUES ("DIYA","DA",289)"""
#cursor.execute(InsertData)
#connection.commit()'''

#def userEntry(stdName,stdCourse,rollno):
#  insertQuery = """INSERT INTO students(stdName,stdCourses,rollno) VALUES (%s,%s,%s)"""
#  record = (stdName,stdCourse,rollno)
#   cursor = connection.cursor()
#   cursor.execute(insertQuery,record)
 #  connection.commit()

#name = input("enter your name: ")
#courses = input("enter your courses: ")
#roll = int(input("enter your rollno "))   

#userEntry(name,courses,roll)

#cursor = connection.cursor()
#sql_select_query = """SELECT * FROM students"""
#cursor.execute(sql_select_query)
#records = cursor.fetchall()
#print(type(records))
#for data in records:
#    print(data)
print("You are wrong")
print("I am Kirti")

def updateData(rollNo,id):
    updateQuery = """UPDATE students SET rollNo = %s where id=%s"""
    updateVar = (rollNo,id)
    cursor = connection.cursor()
    cursor.execute(updateQuery,updateVar)
    connection.commit()
updateData(286,4)    
    











