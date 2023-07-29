from twilio.rest import Client

client = Client("AC47b584cabd415aff407e864ce4830390",
                "c500f72e3d0fd0a53163ef849994b92c"
) 

#Read alll messages
# for msg in client.messages.list():
#     print(msg.body)


#Create and send a message
# msg = client.messages.create(
#     to="+16468539912",
#     from_="+19893003254",
#     body= "Hello! This is the second message sent by Python"
# )
# print(f"Create a new message: {msg.sid}")

#Delete Messages
for msg in client.messages.list():
    print(f"Deleting {msg.body}")
    msg.delete()