import socket

def mainClient():
    '''client stuff'''
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # get local machine name
    host = socket.gethostname()                           
    port = 9000
    # connection to hostname on the port.
    s.connect((host, port))    
    dataToSend = "hello server from client"
    s.send(dataToSend)                           
    # Receive no more than 1024 bytes
    tm = s.recv(1024)  
    print("data got from server: %s" % tm.decode('ascii'))                                   
    s.close()

if __name__ == "__main__":
    mainClient()



