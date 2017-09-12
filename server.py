import socket                                         
import time

def mainServer():
    '''server stuff'''
    mainfile = open('DB_file','a')
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    host = socket.gethostname() 
    port = 9000
    #binded two strings together - form the address
    serversocket.bind((host, port))
    #need to listen to up to 5 requests
    serversocket.listen(5)  
    print("Listening...")
    while True:
        # establish a connection
        clientsocket, addr = serversocket.accept()      
        print("Got a connection from %s" % str(addr))
        data = clientsocket.recv(1024)
        if not data: 
            pass
        else:
            #clientsocket.send(data.encode('ascii'))
            clientsocket.close()

if __name__ == "__main__":
    mainServer()