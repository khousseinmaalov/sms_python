from ipaddress import IPv4Address
from pyairmore.request import AirmoreSession
from pyairmore.services.messaging import MessagingService
from time import sleep

k = 0
l = 0
liste = ["oui", "non"]
listee = ["vrai", "faux"]

ip = IPv4Address("votre ip")
session = AirmoreSession(ip)
was_accepted = session.request_authorization()

service = MessagingService(session)
messages = service.fetch_message_history()
a = messages[0].content

while 1:
  sleep(1)
  messages = service.fetch_message_history()
  print(a,l)
  if a == messages[0].content:
    pass
  else:
    if messages[0].phone == "le numero":
      if messages[0].content != liste[l-1]:
        service.send_message("le numero", liste[l])
        a = messages[0].content
        print(a,l)
        l = l+1
        if l == len(liste):
          l = 0
    else:
      if messages[0].content != liste[k-1]:
        service.send_message(messages[0].phone, liste[k])
        a = messages[0].content
        print(a,k)
        k = k+1
        if k == len(listee):
          k = 0
