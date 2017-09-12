import socket                                         
import time




def SendError(cs):
    '''something went wrong :p'''
    error = "ERROR"
    cs.send(error.encode('ascii'))
    return cs
   
def CloseConnection(cs):
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


def SearchSentence(cs,sentence):
    ''' Search for a sentence in a file'''
    found = False
    mainfile = open('DB_file.txt','r')
    lines = mainfile.readlines()
    mainfile.close()
    for line in lines:
        if line == sentence +"\n":
            found = True
    if found:
        cs = SendOK(cs)
    else:
        cs = SendError(cs)
    return cs

def RemoveSentence(cs,sentence):
    ''' Remove a sentence from the file, if it exists ofc'''
    found = False
    mainfile = open('DB_file.txt','r')
    lines = mainfile.readlines()
    mainfile.close()
    mainfile = open('DB_file.txt','w')
    for line in lines:
        if line != sentence +"\n":
            mainfile.write(line)
        else:
            found = True
    mainfile.close()
    if found:
        cs = SendOK(cs)
    else:
        cs = SendError(cs)
    return cs

def mainServer():
    '''server stuff'''
    #mainfile = open('DB_file.txt','a')
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    host = socket.gethostname() 
    port = 9000
    #binded two strings together - form the address
    serversocket.bind((host, port))
    #need to listen to up to 5 requests in queue
    serversocket.listen(5)  
    print("Listening...")
    #listen to incomming clients
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
                clientsocket = SendError(clientsocket)
            else:
                if data_recieved == "disconnect":
                    clientsocket = CloseConnection(clientsocket)
                    break
                if data_recieved[0:3] == "add":
                    clientsocket = AddSentence(clientsocket,data_recieved[4:])
                if data_recieved[0:6] == "remove":
                    clientsocket = RemoveSentence(clientsocket,data_recieved[7:])
                if data_recieved[0:6] == "search":
                    clientsocket = SearchSentence(clientsocket,data_recieved[7:])

        #clientsocket.send(data.encode('ascii'))
        #clientsocket.close()

if __name__ == "__main__":
    mainServer()