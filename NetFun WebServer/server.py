#import python socket library
from socket import *
#import sys module
import sys
#Prepare a server socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 80
serverSocket.bind(('', serverPort)) #bind socket to port 80
serverSocket.listen(1)
print("Webserver is on port: ", serverPort)

while True: #loop
    #Establish the connection
    print("Ready to serve")
    connectionSocket, addr = serverSocket.accept() #server waits on accept() for incoming requests, new socket created on return
    try:
        message = connectionSocket.recv(1024) #
        filename = message.split()[1] #split string message into list, return element at index 1
        f = open(filename[1:]) #
        outputdata = f.read()
        #Send the content of the required file to the client
        connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n") 
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
        print("Message Successfully Sent")
    except IOError: 
        #Send response message for file not found
        connectionSocket.send(b"HTTP/1.1 404 Not Found\r\n\r\n")
        connectionSocket.send(b"<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n") #print in html page
        print("404 Error not Found")
        #Close client socket
        connectionSocket.close()
    serverSocket.close()
    sys.exit() #exit
