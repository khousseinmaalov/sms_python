from ipaddress import IPv4Address
from pyairmore.request import AirmoreSession
from pyairmore.services.messaging import MessagingService
from time import sleep


x = input("ip locale: ")
y = input("numéro cible: ")
z = input("message: ")
snk = int(input("nb de réptésions: "))

ip = IPv4Address(x)
session = AirmoreSession(ip)
was_accepted = session.request_authorization()

service = MessagingService(session)

a = 0

while a < snk:
	service.send_message(y, z)
	a = a+1
