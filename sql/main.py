from function import *
from bridge import *
from ERROR import *
from filetype import *
from fileos import *
from multiprocessing import *
from protect import *
import time
import os

def main():
    try:
        hs = []
        password, username = log()
        if password == getpassword(username)[1]:
            useryn = "#" if getpassword(username)[3] == 1 else "$"
            while True:
                string = input("{}@{}--{}:".format(username, getpassword(username)[2], useryn))
                writeit(string)
                hs.append(string)
                if string == "adduser":
                    if useryn == "$":
                        print("You are not root.")
                    elif useryn == "#": 
                        adduser()
                elif string == "exit":
                    break
                elif string == "changeuser":
                    main()
                elif string == "out":
                    out()
                elif string == "calculator":
                    cal()
                elif string == "errorget":
                    errorget()
                elif string == "history":
                    history()
                elif string == "termux":
                    if useryn == "$":
                        print("You are not root.")
                    elif useryn == "#":
                        os_operation()
                elif string == "fileos":
                    fileos()
                elif string == "list":
                    print('''
                    adduser
                    changeuser
                    history
                    termux
                    calculator
                    errorget
                    list
                    out
                    fileos
                          ''')
                elif string == " ":
                    print(hs[len(hs)-2])
            print("Exiting...")
        else:
            main()
    except Exception as e:
        i = 0
        i += 1
        errortime = time.localtime()
        filepath = os.path.basename(__file__)
        errorwrite(errortime, filepath, "function main()", i)
        print("Something went wrong! Resetting...")
        main()

if __name__ == "__main__":
    process1 = Process(target=mainpro)
    process1.start()
    main()
    process1.join()
    process1.close()
