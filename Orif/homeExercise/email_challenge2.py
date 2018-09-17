import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("YOUR EMAIL ADDRESS", "YOUR PASSWORD")

msg = "Hello, This message has been send from Python!"
server.sendmail("YOUR EMAIL ADDRESS", "THE EMAIL ADDRESS TO SEND TO", msg)
server.quit()


#This setting is not available for accounts with 2-Step Verification enabled. 
# Such accounts require an application-specific password for less secure apps access.