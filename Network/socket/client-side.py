import socket
try:
    #Connection protocol type UDP or TCP here is a TCP 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 12345
    s.connect((host,port))
    msg = s.recv(1024) #defines the maximum data 
    s.close()
    print(msg.decode('ascii'))
except:
    print("First run server side")
