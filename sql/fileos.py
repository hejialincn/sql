import os
import hashlib
from filetype import *

def gui():
    print("Please enter things!")
    enter = input("connect: ")
    print("Got it!")
    mode = input("Mode: ")
    if mode == "q!":
        pass
    if mode == "q":
        return enter

def write_line(name, path):
    with open(path, "a") as file:
        file.write(name + "\n")

def write_file(path, name, conn):
    mode = "w" if os.path.exists(path + name) else "x"
    with open(path + name, mode) as file:
        file.write(conn)

def read_file(path):
    with open(path, "r") as file:
        return file.readline()

def process_file(get1, path, string):
    write_line(get1, path)
    ftype = typechoose(string)
    file_type(ftype, get1)

def fileos():
    while True:
        string = ""
        get = input("file_code: ")

        if get == "new":
            get1 = input("filename: ")
            path = "/home/he/sql/data/file type/SAFE"
            write_line(get1, path)
            ftype = typechoose("system")
            file_type(ftype, get1)
            path = "/home/he/sql/file"
            enter = gui()
            write_file(path, get1, enter)  

        if get == "import":
            get1 = input("filename: ")
            get2 = input("trusted? [y/n]: ")
            if get2.lower() in ["y", "yes"]:
                path = "/home/he/sql/data/file type/WRING"
                process_file(get1, path, "trusted")
                get3 = input("copy filepath: ")
                connect = read_file(get3)
                write_file("/home/he/sql/file", get1, connect)
            else:
                path = "/home/he/sql/data/file type/DANGEROUS"
                process_file(get1, path, "untrusted")
                get3 = input("copy filepath: ")
                connect = read_file(get3)
                write_file("/home/he/sql/file", get1, connect)

        if get == "get":
            get1 = input("filename: ")
            get2 = input("visa? [path/none]: ")
            
            if get2.lower() in ["none", "n"]:
                path = "/home/he/sql/data/file type/DANGEROUS"
                process_file(get1, path, "untrusted")
            else:
                string = read_file(get2)
                get3 = input("path (file): ")
                connect1 = read_file(get3)
                connect = hashlib.sha1(str(connect1).encode("utf-8")).hexdigest()
                print(f"{string}\n{connect}")
                if string == connect:
                    path = "/home/he/sql/data/file type/WRING"
                    process_file(get1, path, "visa?")
                    write_file("/home/he/sql/file", get1, connect1)
                else:
                    print("Visa cannot be used")
                    path = "/home/he/sql/data/file type/DANGEROUS"
                    write_line(get1, path)
                    ftype = typechoose("untrusted")
                    file_type(ftype, get1)
                    process_file(get1, path, "untrusted")
                    connect1 = read_file(get3)
                    write_file("/home/he/sql/file", get1, connect1)

        if get == "exit":
            print("Exiting...")
            break
