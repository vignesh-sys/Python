#Sample python script to find the memory utlization of a windows machine and send and email if it exceeds the threshold.

#Importing the required libraries
import psutil
import smtplib

#Set the threshold limit
mem_threshold = 80

#Get the mem utilization of the machine.
mem_usuage = psutil.virtual_memory().percent

if(mem_threshold > mem_usuage):

    #create smtp session
    email = smtplib.SMTP('smtp.gmail.com', 587)

    #TLS for security
    email.starttls

    #authentication
    email.login("Sender Email Address", "Password") 

    #message
    message = "Your Memory utilization is" + str(mem_usuage)

    #sendmail
    email.sendmail("Sender Email Address", "Recepient Email Address", message)

    #exist 
    email.quit()

else:
    pass

  

