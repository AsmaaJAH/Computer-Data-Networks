from socket import *
serverPort = 2000
serverIP= '127.0.0.1'
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverIP,serverPort))

#clients to listen to them:
serverSocket.listen(1)

print("Server listening on",serverIP,":",serverPort)
while True:
    connectionSocket, addr = serverSocket.accept()
    received_client_msg = connectionSocket.recv(1024)
    print("Connection has been established with:", addr)
    received_client_msg = received_client_msg.decode("UTF-8")
    print('Client is connected from {}:\n{}\n\n' .format( addr , received_client_msg ) )
    print("Client received message:", received_client_msg)
    connectionSocket.close()