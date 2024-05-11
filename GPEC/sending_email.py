from uploading import uploading_file
import smtplib
from email.mime.text import MIMEText


import smtplib
def send_email(link):
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login("f20210080@dubai.bits-pilani.ac.in", "oaf-cocoa2-fish-footgear")
    # message to be sent
    message = f"Hi there! This is a test email.{str(link)}"
    # sending the mail
    s.sendmail("f20210080@dubai.bits-pilani.ac.in", "f20210132@dubai.bits-pilani.ac.in", msg=message)
    # terminating the session
    s.quit()
    print("email sent successfully")



