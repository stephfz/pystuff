from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACd67ca64c7f49874f61218200f3622cd9"
auth_token  = "564f187f2ab1e87c5bc1e991823a4dfc"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Alo Python?",
    to="+51997270000",    # Replace with your phone number
    from_="+16692315604") # Replace with your Twilio number
print message.sid
