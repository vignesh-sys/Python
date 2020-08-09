#Sample python script to find the cpu utlization of a windows machine and send and email if the cpu exceeds the threshold.

#Importing the required libraries
import psutil
import smtplib

#Set the cpu threshold limit
cpu_threshold = 80

#Get the cpu usage of the machine in percentage
cpu_usage = psutil.cpu_percent()

if (cpu_usage > cpu_threshold):
    #create smtp session
    email = smtplib.SMTP('smtp.gmail.com', 587)

    #TLS for security
    email.starttls

    #authentication
    email.login("Sender Email Address", "password")

    #message
    message = "CPU_threshold is" + str(cpu_threshold)

    #sendmail
    email.sendmail("Sender Email Address", "Recipient Email Address", message)

    #terminating the session
    email.quit()
else:
    pass



