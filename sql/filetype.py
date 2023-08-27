import os
from function import *

def newtype(name,ftype):
    con=sql.connect("/home/he/sql/data/student.db")
    cur=con.cursor()
    code="INSERT INTO file VALUES('{}','{}')".format(name,ftype)
    print(code)
    cur.execute(code)
    con.commit()
def file_type(string,name):
    if string=="safe":
        ftype=0
        newtype(name,ftype)    
    if string=="warning":
        ftype=1
        newtype(name,ftype)
    if string=="dangerous":
        ftype=2
        newtype(name,ftype)
def typechoose(string):
    if string=="system" or string =="user":
        ftype="safe"
    if string=="trusted" or string =="visa?":
        ftype="warning"
    if string=="foreign" or string =="untrusted" :
        ftype="dangerous"
    return(ftype)    