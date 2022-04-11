import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="radha123"
)

print(mydb)
INSERT INTO mysql.user (Host, User, Password) VALUES ('%', 'root', 'radha123');
GRANT ALL ON . TO 'root'@'%' WITH GRANT OPTION;