from socket import *
import time

udp_address = "127.0.0.1"
udp_port = 12000
addr = (udp_address, udp_port)
nr_recv = 0
max_time = 0
min_time = 10
sum_time = 0
BEAT_PERIOD = 3
sock = socket(AF_INET, SOCK_DGRAM)
sock.settimeout(1)
index = 0
count = 0
while True:
    count +=1
    index +=1
    curtime =  time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    mesg = "ping %d "%index + "\t" + curtime
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
        time.sleep(BEAT_PERIOD)
    except Exception as e:
        print "Request timed out"
        print "retry send the message index %d"%index
        index -=1
        continue 
    except KeyboardInterrupt:
        print "minimum %f ms, maximum %f ms, average %f ms " %(min_time*1000, max_time *1000, sum_time / float(nr_recv) * 1000)
        pck_loss = (float(count-nr_recv))/float(count) * 100.0
        print "packet loss rate is %d" %(pck_loss) + "%"
        exit()

sock.close()

