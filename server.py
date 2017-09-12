import socket                                         
import time




def errorRecieving(cs):
    '''something went wrong :p'''
    error = "ERROR"
    cs.send(error.encode('ascii'))
    return cs
   
def closeConnection(cs):
    '''closing the connection'''
    close = "close"
    cs.send(close.encode('ascii'))
    cs.close()
    return cs

def AddSentence(cs, sentence):
    ''' Appended a sentence to the DB_file'''
    mainfile = open('DB_file.txt','a')
    mainfile.write(sentence + '\n')
    mainfile.close()
    cs = SendOK(cs)
    return cs
    
def SendOK(cs):
    okmsg = "ok"
    cs.send(okmsg.encode('ascii'))
    return cs


def mainServer():
    '''server stuff'''
    #mainfile = open('DB_file.txt','a')
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    host = socket.gethostname() 
    port = 9000
    #binded two strings together - form the address
    serversocket.bind((host, port))
    #need to listen to up to 5 requests
    serversocket.listen(5)  
    print("Listening...")

    #data = clientsocket.recv(1024)
    while True:
         # establish a connection
        clientsocket, addr = serversocket.accept()      
        print("Got a connection from %s" % str(addr))
        #send ok for success client connection
        clientsocket = SendOK(clientsocket)
        while True:
            #start listening to orders from the client
            data_recieved = clientsocket.recv(1024)
            if not data_recieved:
                clientsocket = errorRecieving(clientsocket)
            else:
                if data_recieved == "disconnect":
                    clientsocket = closeConnection(clientsocket)
                    break
                if data_recieved[0:3] == "add":
                    clientsocket = AddSentence(clientsocket,data_recieved[4:])

        #clientsocket.send(data.encode('ascii'))
        #clientsocket.close()

if __name__ == "__main__":
    mainServer()