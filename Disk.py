#Simple python script to find the Disk usage and send mail if it exceeds the threshold
#Importing the required libraries
import psutil
import smtplib

#Set threshold value
Disk_threshold = 80

#Disk names
Disk_array = ["D:","C:"]

for i in Disk_array:

    d_usage = psutil.disk_usage(i).percent
    
    if (Disk_array > d_usage):
        #create smtp session
        email = smtplib.SMTP('smtp.gmail.com', 587)

        #TLS for security
        email.starttls

        #authentication
        email.login("Sender Email Address", "Password") 

        #message
        message = "Your Disk utilization is" + str(d_usuage)

        #sendmail
        email.sendmail("Sender Email Address", "Recepient Email Address", message)

        #exist 
        email.quit()
    else:
        pass