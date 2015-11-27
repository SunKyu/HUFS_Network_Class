from socket import *
import time

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))

CHECK_TIME = 15
max_index = 0
min_index = 0
message, address = serverSocket.recvfrom(1024)
print message
serverSocket.settimeout(CHECK_TIME)
while True:
    try:
        message, address = serverSocket.recvfrom(1024)
        print message
    except Exception as e:
        print e
        print "time out and client is dead"
        exit()
    
