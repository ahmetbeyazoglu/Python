import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
h_ip = str(raw_input("Url: "))
h_port = int (input("Port: "))

s.connect((h_ip,h_port))
s.send(b'GET /\n\n')

banner = s.recv(1024)
print '[+]' +str(banner)