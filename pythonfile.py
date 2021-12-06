import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="wordpresswebsite",
  password=""
)
mycursor=mydb.cursor()
print("\n PRINT TABLE");
mycursor.execute("SELECT * FROM datas")
myresult=mycursor.fetchall()
for x in myresult:
    print(x)


#CREATE INDEX
# mycursor.execute("CREATE INDEX index_created ON data(keyword,filename)")
# print("\n1. Index created")
mycursor.execute("DROP INDEX index_created ON datas")
print("\nIndex dropped")


#FIND KEYWORD AND FILES
mycursor.execute("SELECT filename FROM datas WHERE keyword='ai'")
myresult=mycursor.fetchall()
print("\n2. LIST OF FILES")
for x in myresult:
    print(x)

#DISPLAY CONTENT OF FILE
print("\n3. CONTENT OF FILE")
mycursor.execute("SELECT path FROM datas WHERE filename='intersection over union (1).htm'")
myresult=mycursor.fetchall()
for x in myresult:
    print(x)
    str = ''.join(x)

# print(str)
f = open(str, "r")
print(f.read())

