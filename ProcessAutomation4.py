import psutil
import os
import time
from sys import *
import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def EmailSend(log_dir,email):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "aditi.pujari91@gmail.com"  # Enter your address
    receiver_email = email  # Enter receiver address
    password = "xycaitfszwlavpuq"

    msg = MIMEMultipart()
    subject = "An email with attachment from Python"
    body = "This is an email with attachment sent from Python"
    msg['Subject'] = "Automation Script having process file attachment"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Add body to email
    msg.attach(MIMEText(body, "plain"))

    filename = os.path.join(os.getcwd(),log_dir)

    files = os.listdir(filename)
    # Open file in binary mode
    for file in files:
        file_path = os.path.join(filename,file)
        with open(file_path, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {file}",
    )

    # Add attachment to message and convert message to string
    msg.attach(part)
    text = msg.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

        print("Email Sent Successfully")


def ProcessDisplay(log_dir, email):

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

    EmailSend(log_dir,email)

def main():
    print("---------------Automations--------------------")
    print("Automation Script started with name : ", argv[0])


    if (len(argv) != 3):
        print("Error : Insufficient arguments")
        print("Use -h for help and -u for usage of the script")
        exit()

    if ((argv[1] == "-h") or (argv[1] == "-H")):
        print("Help : The script is used for log record of running processes and send log file via email")
        exit()

    elif ((argv[1] == "-u") or (argv[1] == "-U")):
        print("Usage : ApplicationName AbsolutePath_of_Directory email_id")
        exit()

    try:
        ProcessDisplay(argv[1],argv[2])

    except ValueError:
        print("Error: Invalid datatype of input")

    except Exception as e:
        print("Invalid Input", e)


if __name__ == "__main__":
    main()