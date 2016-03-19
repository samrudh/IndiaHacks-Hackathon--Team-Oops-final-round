import socket
import time
import string

#print ("UDP target IP:", udp_ip)
#print ("UDP target port", udp_port)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


udp_ip = "192.168.43.240" #192.168.43.240"#"192.168.43.175" #"127.0.0.1" 
udp_port = 5055 #8088
time.sleep(3)
sock.settimeout(300)
with open ('input10.txt', 'r') as inputfile:	
	for line in inputfile:
		#line= inputfile
		msg = str(line)

		print ("message:", msg)
		time.sleep(2)
		sock.sendto(msg.encode(), (udp_ip, udp_port))
print ("sent")

