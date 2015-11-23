from socket import *
import time

udp_address = "127.0.0.1"
udp_port = 12000

sock = socket(AF_INET, SOCK_DGRAM)
for i in range(11):
    try:
    
        begin = time.time()
        sock.sendto("ping %d" %i, (udp_address, udp_port))
        sock.settimeout(1)
        data = sock.recvfrom(1024)
        end = time.time()
        print data
        print "RTT time = ", begin - end
    except Exception as e:
        print "Request timed out"
        print e
        sock.close()
