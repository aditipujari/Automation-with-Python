import psutil
import os
import time
from sys import *

def ProcessDisplay(log_dir = "Marvellous"):

    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    seperator = "-"*80
    log_path = os.path.join(log_dir,"MarvellousLog.log")
    f = open(log_path,"w")
    f.write(seperator+"\n")
    f.write("Marvellous Infosystem process Logger:\n")
    f.write(seperator+ "\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs = ['pid', 'name','username'])
            pinfo['vms'] = proc.memory_info().vms/ (1024*1024)
            listprocess.append(pinfo)

        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n"%element)


def main():
    print("---------------Automations--------------------")
    print("Automation Script started with name : ", argv[0])

    #argv[1]= os.path.abspath(os.getcwd())

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