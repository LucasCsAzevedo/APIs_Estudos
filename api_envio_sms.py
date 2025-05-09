import os
from twilio.rest import Client

account_sid = os.getenv('account')
auth_token = os.getenv('auth')

client = Client(account_sid, auth_token)

remetente = os.getenv('remetente')
destino = os.getenv('destino')

message = client.messages.create(
    to = destino,
    from_ = remetente,
    body ='Como isso é legal!!!!!!'
)

print(message.sid)