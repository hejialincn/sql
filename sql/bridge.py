import os
#import lib

#function
def writehistory(connect):
    with open("/home/he/sql/data/history","a") as f:
        f.writelines(connect+"\n")  

#main function
def os_operation():
    bash=[]
    ter=[]
    while True:
        string = ""
        string=input("code:")
        ter.append(string)
        writehistory(string)
        if string == " ":
            print(ter[len(ter)-2])
        if string == "where":
            print(os.getcwd())
        if string == "at?":
            name = input("文件名: ")
            print(os.path.exists(os.getcwd() + '/' + name))
        if string == "file":
            code = input("[新建:n/删除:d]: ")
            writehistory(code)
            if code == "n":
                name = input("文件名: ")
                os.system("touch " + os.getcwd() + '/' + name)
                print("文件创建成功。")
            if code == "d":
                name = input("文件名: ")
                os.system("rm " + os.getcwd() + '/' + name)
                print("文件删除成功。")
        if string == "folder":
            code = input("[新建:n/删除:d]: ")
            writehistory(code)
            if code == "n":
                name = input("文件夹名: ")
                os.system("mkdir " + os.getcwd() + '/' + name)
                print("文件夹创建成功。")
            if code == "d":
                name = input("文件夹名: ")
                os.system("rmdir " + os.getcwd() + '/' + name)
                print("文件夹删除成功。")
        if string == "bash":
            while True:
                code=input("shell-$:")
                bash.append(code)
                if code=="exit":
                    break
                if code == "1":
                    print(str(ter[bash(bash)-2])) 
                os.system(code)
        if string == "exit":
            break
        
