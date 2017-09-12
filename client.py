import socket

#global variable to know if socket is open or not
static_if_connected = False
def printMenu():
    ''' menu for work for the client side'''
    print "1. Connect to server"      
    print "2. Search sentence "
    print "3. Add sentence "
    print "4. Delete sentence "
    print "5. Disconnect "
    print "6. Exit "
    #otherwise function will return 'None'
    return ""

def ConnectToServer(sock,host,port):
    '''connection to server on the port'''
    global static_if_connected
    if not static_if_connected:
        sock.connect((host, port)) 
        static_if_connected = True
    return sock

def Disconnect(sock):
    '''disconnect from server'''
    global static_if_connected
    if static_if_connected:
        sock.close()
    return sock

def SearchSentence(sock):

    return sock

def AddSentence(sock):

    return sock

def DeleteSentence(sock):

    return sock


def mainClient():
    '''client stuff'''
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # get local machine name
    host = socket.gethostname()                           
    port = 9000

    while True:
        menuitem = raw_input(printMenu() + ">> ")
        if menuitem == '1':
            s = ConnectToServer(s,host, port)
        if menuitem == '2':
            s = SearchSentence(s)
        if menuitem == '3':
            s = AddSentence(s)
        if menuitem == '4':
            s = DeleteSentence(s)
        if menuitem == '5':
            s = Disconnect(s)
        if menuitem == '6':
            break




    # connection to hostname on the port.
    #s.connect((host, port))    
    #dataToSend = "hello server from client"
    #s.send(dataToSend)                           
    # Receive no more than 1024 bytes
    #tm = s.recv(1024)  
    #print("data got from server: %s" % tm.decode('ascii'))                                   
    #s.close()

if __name__ == "__main__":
    mainClient()



