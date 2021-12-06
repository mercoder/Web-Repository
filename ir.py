import mysql.connector 
import webbrowser

db = mysql.connector.connect(host = 'localhost', user = 'root', passwd = '', database  ='wordpresswebsite')

mycursor = db.cursor()

print("Keywords are : ai, deep learning, computer vision, intersection over union, robotic grasping \n")
Keyword = input("Enter a Keyword : ")
mycursor.execute("select filename from datas where Keyword = '"+Keyword+"';")

for z in mycursor:
    print(z)

Filename = input("Enter a Filename: \n")
mycursor.execute("select path from datas where keyword = '"+Keyword+"' and filename = '"+Filename+"';")

path = ''
for x in mycursor:
    for a in x:
        path = path + a 

print (path)


url = path
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open(url)

# webbrowser.open(url,new=2)
# print("website opened")