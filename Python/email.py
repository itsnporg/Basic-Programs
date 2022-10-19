import smtplib
from email.message import EmailMessage

msg = EmailMessage()
def sendEmail(msgg,From,Passwd):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(From, Passwd)
    server.send_message(msgg)
    server.quit()

# Take inputs from the user
From = input("Enter the email you want to send from: ")
password = input("Enter the password: ")
email_subject = input("Enter the subject to the mail: ")
email_body = input("Enter your message\n")
total_send = int(input("To how many people would you like to send this mail to?:"))

# Initiate process to send email
msg['Subject'] = email_subject
msg['From'] = From
receiver_mails = []
msg['To'] = ['receiver1','receiver2'.....'receiverN']

msg.set_content(email_body)
sendEmail(msg,From,password)