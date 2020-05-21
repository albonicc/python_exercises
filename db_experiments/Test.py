import mysql.connector

def insertStudent():
  add_student = ("INSERT INTO student "
               "(student_id, name, major) "
               "VALUES (%s, %s, %s)")
  mycursor.execute("SElECT student_id FROM student ORDER BY student_id DESC LIMIT 1")
  last_student_id = list(mycursor.fetchone())
  new_student_id = int(last_student_id[-1] + 1)
  new_student =[new_student_id]
  print("Name of the new student:")
  new_student_name = input()
  new_student.append(new_student_name)
  print("Major of the new student:")
  new_student_major = input()
  new_student.append(new_student_major)
  mycursor.execute(add_student, tuple(new_student))
  dbConnect.commit()
  print("Student added successfuly!")

def readStudent():
  print("Enter the id of the student to find")
  student_id = input()
  read_student_id = ("SELECT * FROM student WHERE student_id = %s")
  mycursor.execute(read_student_id, tuple(student_id))
  myresult = mycursor.fetchall()
  for i in myresult:
    print(i)

def updateStudent():
  student_update = []
  print("Enter the id of the student whose information is going to be updated:")
  student_id = input()
  student_update.append(student_id)
  print("Enter student new name:")
  student_name = input()
  student_update.insert(0, student_name)
  print("Enter new student major:")
  student_major = input()
  student_update.insert(0, student_major)
  update_student = ("UPDATE student SET major = %s, name = %s WHERE student_id= %s")
  mycursor.execute(update_student, tuple(student_update))
  dbConnect.commit()
  print("Student updated successfuly!")

def deleteStudent():
  print("Enter the id of the student whose information is going to be deleted:")
  student_id = input()
  delete_student = ("DELETE FROM student WHERE student_id = %s")
  mycursor.execute(delete_student, tuple(student_id))
  dbConnect.commit()
  print("Student deleted successfuly!")

def showDB():
  mycursor.execute("SELECT * FROM student")
  myresult = mycursor.fetchall()
  for i in myresult:
    print(i)

dbConnect = mysql.connector.connect( #Makes the connection to calamardo db
  host="localhost",
  user="root",
  password="Ragnarok98",
  database="calamardo",
  auth_plugin='mysql_native_password'
)

mycursor = dbConnect.cursor(buffered = True)

print("Select the option you want")
print("[1] Insert student in database")
print("[2] Read student in database")
print("[3] Update student in database")
print("[4] Delete student from database")
print("[5] Show database")
print("Press any other key to exit")

while True:
  option = input()
  if option == '1':
    insertStudent()
    print("Insert a new option:")
  if option == '2':
    readStudent()
    print("Insert a new option:")
  if option == '3':
    updateStudent()
    print("Insert a new option:")
  if option == '4':
    deleteStudent()
    print("Insert a new option:")
  if option == '5':
    showDB()
    print("Insert a new option:")
  else:
    break