import mysql.connector


dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='kompjuter1'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE corporation")

print("DONE!")