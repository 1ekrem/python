import http.client, urllib

token = "aet7haniwq1oianior9htkusgx7ho4"
user = "u76cr36fkajmj2329axh1teh8bnc21"

def pushNotificationSender(userMessage):
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
            urllib.parse.urlencode({
                "token": token,
                "user": user,
                "message": userMessage
            }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()

# def pushNotificationSender(token, user, userMessage):
#     conn = http.client.HTTPSConnection("api.pushover.net:443")
#     conn.request("POST", "/1/messages.json",
#                  urllib.parse.urlencode({
#                      "token": token,
#                      "user": user,
#                      "message": userMessage,
#                  }), {"Content-type": "application/x-www-form-urlencoded"})
#     response = conn.getresponse()
#     print(response.read().decode())
#     conn.close()

#pushNotificationSender(userMessage="Test")