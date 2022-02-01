from twilio.rest import Client

# put your own credentials here
account_sid = "put yours here"
auth_token = "put yours here"

client = Client(account_sid, auth_token)

message= client.messages.create(
    to="put yours here",
    from_="put your twilio number here",
    body="SOS! if anyone sees this message! theres a zombie outbreak! meet at the mall! we will group up there!"
)
