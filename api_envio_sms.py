from twilio.rest import Client

account_sid = 'AC36c91629ab47bb53a2ba32996c275c39'
auth_token = '47811de800a61c895d0280e5ca429f11'

client = Client(account_sid, auth_token)

remetente = '+19785747363'
destino = '+5511915611207'

message = client.messages.create(
    to = destino,
    from_ = remetente,
    body ='Como isso é legal!!!!!!'
)

print(message.sid)