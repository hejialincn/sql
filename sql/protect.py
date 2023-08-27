import psutil
import os
import time

def wrget(path, name, conn):
    if os.path.exists(path + name):
        with open(path + name, "w") as w:
            w.writelines(conn)
    else:
        with open(path + name, "x") as w:
            w.writelines(conn)

def read(path):
    with open(path, "r") as r:
        return r.readline()

def find_processes_file(path):
    processes = []
    files = psutil.Process().open_files()
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            for f in files:
                if f.path == path and proc.pid != os.getpid():
                    processes.append(proc)
                    break
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            continue
    return processes

def returnall(file_path):
    controlling_processes = find_processes_file(file_path)
    if controlling_processes:
        return [proc.pid for proc in controlling_processes]
    else:
        return "None"

def protectkill(pid, mode):
    if pid.isdigit():
        proc = psutil.Process(int(pid))
        if mode == 1:
            proc.terminate()
        elif mode == 0:
            proc.kill()

def mainpro():
    i=0
    while True:
        if i==10:
            break
        else:
            i=i+1
            file_list = os.listdir("/home/he/sql/file")
            if not file_list:
                continue
            else:
                pids = []
                for file_name in file_list:
                    pids.extend(returnall("/home/he/sql/file/" + file_name))
                    os.system("lsof -t /home/he/sql/file/{} > /home/he/sql/tmp/tmp_id".format(file_name))
                    pids.extend(read("/home/he/sql/tmp/tmp_id").splitlines())
                    wrget("/home/he/sql/tmp/", "tmp_id", "")
                
                for pid in pids:
                    protectkill(pid, 0)
                    
