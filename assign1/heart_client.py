from socket import *
import time

udp_address = "127.0.0.1"
udp_port = 12000
addr = (udp_address, udp_port)
BEAT_PERIOD = 5

sock = socket (AF_INET, SOCK_DGRAM)
sock.settimeout(1)
index = 0

while True:
    index += 1 
    curtime =  time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    mesg = "ping %d " %index + "  " + curtime
    try:
        sock.sendto(mesg, addr)
    except Exception as e:
        print e
    finally:
        time.sleep(BEAT_PERIOD)
