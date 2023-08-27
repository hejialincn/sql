def errorwrite(time,filename,error,times):
    with open("/home/hejialin/sql/data/ERROR","a") as f:
        f.writelines("错误发生时间:"+str(time)+"\t"+"错误文件地址:"+filename+"\t"+"错误函数:"+error+"\t"+"当前程序的第＊次错误:"+str(times)+"\n") 
def errorget():
    with open("/home/hejialin/sql/data/ERROR","r") as f:
        for i in f.readlines():
            print(i)
    
