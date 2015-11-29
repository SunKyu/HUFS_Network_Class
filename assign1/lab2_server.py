from socket import *
import time
import random

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))

CHECK_TIME = 9
max_index = 0
min_index = 0 
serverSocket.settimeout(CHECK_TIME)
befotime = 0
thistime = 0
miss_check_time = time.time()
miss_list = set()
while True:
    rand = random.randint(0, 10)    
    try:
        message, address = serverSocket.recvfrom(1024)
        if rand < 4: 
            miss_list.add(int(message.split()[1]))
            continue
        index = int(message.split()[1])
        miss_list.discard(index)
        message = message.upper()
        if befotime:
            befotime = thistime
        else:
            befotime = time.mktime(time.strptime(message.split('\t')[1], "%Y-%m-%d %H:%M:%S"))
        thistime = time.mktime(time.strptime(message.split('\t')[1], "%Y-%m-%d %H:%M:%S"))
        term_time = thistime - befotime
        print "diffrence time : %d" %(int(term_time))
        
        serverSocket.sendto(message, address)
    except timeout:
        print e
        print "timeout, so cleint is dead"
        exit()
    except Exception as e:
        print e
        exit()
    finally:
        if (time.time() - miss_check_time) > CHECK_TIME and len(miss_list)>0:
            print ("missing Ping numbers ")
            for i in range(len(miss_list)):
                print (miss_list.pop()),
            print ""
            miss_check_time = time.time()
