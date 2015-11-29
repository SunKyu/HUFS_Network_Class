from socket import *
import random

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))

CHECK_TIME = 9
max_index = 0
min_index = 0 
serverSocket.settimeout(CHECK_TIME)

while True:
    rand = random.randint(0, 10)    
    try:
        message, address = serverSocket.recvfrom(1024)
        message = message.upper()
        if rand < 4:
            continue
        serverSocket.sendto(message, address)
    except Exception as e:
        print e
        print "timeout so cleint is dead"
        exit()
