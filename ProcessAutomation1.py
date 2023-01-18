import psutil

# Python Application to give the information of running processes

def ProcessDisplay():
    listprocess = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs = ['pid', 'name','username'])
            listprocess.append(pinfo)

        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return listprocess

def main():
    print("Python Automation Script")

    listprocess = ProcessDisplay()

    for ele in listprocess:
        print(ele)

if __name__ == "__main__":
    main()