from socket import *
import time

udp_address = "127.0.0.1"
udp_port = 12000
addr = (udp_address, udp_port)
nr_recv = 0
max_time = 0
min_time = 10
sum_time = 0
sock = socket(AF_INET, SOCK_DGRAM)
sock.settimeout(1)
for i in range(10):
    curtime =  time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    mesg = "ping %d "%i + " " + curtime
    begin = time.time()
    sock.sendto(mesg , addr)
    try:
        data, server = sock.recvfrom(1024)
        end = time.time()
        nr_recv +=1
        rtt_time = end - begin
        sum_time += rtt_time
        if rtt_time > max_time:
            max_time = rtt_time
        if rtt_time < min_time:
            min_time = rtt_time
        print data + "RTT time = %f ms" % (rtt_time*1000) 
    except Exception as e:
        print "Request timed out"

sock.close()
print "minimum %f ms, maximum %f ms, average %f ms " %(min_time*1000, max_time *1000, sum_time / float(nr_recv) * 1000)
pck_loss = (10-nr_recv) * 10
print "packet loss rate is %d" %(pck_loss) + "%"

