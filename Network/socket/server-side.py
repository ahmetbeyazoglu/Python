import socket

def main():
    host = socket.gethostname()
    port = 12345
    serversocket = socket.socket()
    serversocket.bind((host,port)) #binds the adress to the socket
    serversocket.listen(1) #listens to the connections made to the socket
    print('Socket is listening')
    try:
        while True:
            conn, addr = serversocket.accept() # accept TCP client connection before this we must use the those socket.bind() and socket.listen()
            print("Got Connection from %s" % str(addr))
            msg = 'Connection Established'+ "\r\n"
            conn.send(msg.encode('ascii'))
    except:
        print("Connection Closed")
if __name__=='__main__':
    main()
