from ipadress import IPv4Address
from pyairmore.request import AiremoreSession
from pyairmore.services.messaging import MessagingService
from time import sleep


x = input("ip locale: ")
y = input("numéro cible: ")
z = input("message: ")

ip = IPv4Adrress(x)
session = AirmoreSession(ip)
was_accepted = session.request_authorization()

service = MessagingService(session)

a = 0

while a < 10:
	service.send_message(y, z)
