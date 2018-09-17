

def sendEmail(your_email, your_password, to_email, subject, msg_text ):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText    
    
    MY_ADDRESS = your_email
    MY_PASSWORD = your_password
    RECEIVER = to_email

    server = smtplib.SMTP('smtp.aol.com', 587)
    server.starttls()
    server.login(MY_ADDRESS, MY_PASSWORD)

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = your_email
    msg['To'] = to_email
    msg.attach(MIMEText(msg_text, 'plain'))

    server.sendmail(MY_ADDRESS, RECEIVER , msg.as_string())
    server.quit()


#This setting is not available for accounts with 2-Step Verification enabled. 
# Such accounts require an application-specific password for less secure apps access.

sendEmail("burhannyc@aol.com", "2058007e", "ersaekrem@gmail.com","Python Email Script","Hello")