# 1) create a zip file
# 2) read that zip file contents
# 3) compose a email with above contents
# 4) send the email


import random
import zipfile
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# we are going to use the existing squares.txt file

# time.time() always genereates a unique value, that's why we are using it
# but, since it alwayss gives us a different value, we need to memorize it,
# because later when we read the zip file we will need that name

txt_file_name = "squares.txt"
# Random number is created to uniquely identify the file
random = random.randint(0, 20)
# Create the zip file with random number
zip_name = 'test' + str(random) + '.zip'

# 1) create a zip file
archive = zipfile.ZipFile(zip_name, 'w')  # Openinng the file in the write mode
archive.write(txt_file_name)
archive.close()  # Closing zip file helps it to memorize the value entered.

# 2) read that zip file contents
txt_contents= []
sourceZipFile = zipfile.ZipFile(zip_name, 'r')# Openinng the file in the read mode
with sourceZipFile.open(txt_file_name) as txtFile:
    lines = txtFile.readlines()
    for line in lines:
        txt_contents.append(line.decode('ascii'))

# 3) compose a email with above contents
email_contents = "Here are your squares:\r\n"
for line in txt_contents:
    email_contents = email_contents + line
print(email_contents)

# 4)
# set up the SMTP server
MY_ADDRESS = "pythonchallenge@outlook.com"
PASSWORD = "12345678Aa"
RECEIVER = "pythonchallenge@outlook.com"

s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)

msg = MIMEMultipart()       # Create a message

# setup the parameters of the message
msg['From'] = MY_ADDRESS
msg['To'] = RECEIVER
msg['Subject'] = "Squares"

# add in the message body
msg.attach(MIMEText(email_contents, 'plain'))

# send the message via the server set up earlier.
s.send_message(msg)


