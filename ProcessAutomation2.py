import psutil
from sys import *

# Python Application to give the information of running process asked by the user

def ProcessDisplay(process_name):
    flag = 0
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs = ['pid', 'name','username'])
            #print(pinfo)
            if(pinfo['name'].lower() == process_name.lower()+".exe"):
                print("The information of the running process is :")
                print(pinfo)
                flag = 1
                
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    if(flag == 0):
        print("No such process is running")

def main():

    print("Python Automation Script")
    if (len(argv) != 2):
        print("Error : Insufficient arguments")
        print("Use -h for help and -u for usage of the script")
        exit()

    if ((argv[1] == "-h") or (argv[1] == "-H")):
        print("Help : The script is used for log record of running processes")
        exit()

    elif ((argv[1] == "-u") or (argv[1] == "-U")):
        print("Usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        ProcessDisplay(argv[1])

    except ValueError:
        print("Error: Invalid datatype of input")

    except Exception:
        print("Invalid Input")

if __name__ == "__main__":
    main()