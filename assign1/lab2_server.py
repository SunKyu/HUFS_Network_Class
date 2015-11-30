from socket import *
import time
import random

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))

CHECK_TIME = 9 #heartbeat check time
serverSocket.settimeout(CHECK_TIME)
befotime = 0 #for time difference
thistime = 0 #for time difference
miss_check_time = time.time()
miss_list = set() #use set structre to check missing sequence of ping
while True:
    rand = random.randint(0, 10)    
    try:
        message, address = serverSocket.recvfrom(1024)
        if rand < 4: #make loss
            miss_list.add(int(message.split()[1])) #add sequence num to set
            continue
        index = int(message.split()[1]) #parsing sequnce num
        miss_list.discard(index) #discard sequncenum from set
        message = message.upper()
        if befotime: #calculate differnce
            befotime = thistime
        else:
            befotime = time.mktime(time.strptime(message.split('\t')[1], "%Y-%m-%d %H:%M:%S"))
        thistime = time.mktime(time.strptime(message.split('\t')[1], "%Y-%m-%d %H:%M:%S"))
        term_time = thistime - befotime
        print "diffrence time : %d" %(int(term_time))
        
        serverSocket.sendto(message, address)
    except timeout:
        print "timeout, so cleint is dead"
        exit()
    except Exception as e:
        print e
        exit()
    finally:#check periodic about loss packet
        if (time.time() - miss_check_time) > CHECK_TIME and len(miss_list)>0:
            print ("missing Ping numbers ")
            for i in range(len(miss_list)):
                print (miss_list.pop()),
            print ""
            miss_check_time = time.time()
