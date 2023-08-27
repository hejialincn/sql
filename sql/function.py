import sqlite3 as sql
import hashlib
import os
#import lib
with open()
path=
#system main use these function
def start():
    global con
    con=sql.connect("/home/he/sql/data/student.db")
    global cur
    cur=con.cursor()

def new(name) :
    start()
    cur.execute("CREATE TABLE {}(name text,ftype text)".format(name))

def adduser():
    start()
    user=str(input("username:"))
    password=str(input("password:"))
    root=eval(input("root?[y:1,n:0]:"))
    hash1=hashlib.sha1(password.encode("utf-8")).hexdigest()
    code="INSERT INTO user VALUES({},{},{},{})".format('"'+user+'"','"'+password+'"','"'+hash1+'"',root)
    print(user,password,hash1,root)
    print(code)
    cur.execute(code)
    con.commit()
    con.close()
    os.system("sudo mkdir /home/he/sql/user/{}".format(user))
    with open("/home/he/sql/user/ukey","a") as f:
        f.writelines("/home/he/sql/user/{}".format(user)+"\n")
def getpassword(value):
    start()
    cur.execute("SELECT *FROM user")
    for row in cur.fetchall():
        if value in row[0]:
            return(row)
    con.close()

def log():
    username=input("user:")
    if username=="new":
        adduser()
        username=input("user:")
    if username=="auto":
        return("hejialin123","he")
    password=input("password:")
    return(password,username)

def out():
    string=input("enter:")
    print(string)

def cal():
    while True:
        string=input("enter:")
        if string=="exit":
            break
        print(eval(string))

def history():
    with open("/home/he/sql/data/history","r") as f:
        for i in f.readlines():
            print(i)

def writeit(string):
    with open("/home/he/sql/data/history","a") as f:
        f.writelines(str(string)+"\n")

def message():
    #this function isn't ready 
    pass        


    
