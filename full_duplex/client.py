import sys
import select
import socket
port = 2005
ip = '127.0.0.1'
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
input = [sock,sys.stdin]
while True:
         inputready,outputready,exceptready = select.select(input,[],[])
         for s in inputready:
             if s == sock:
                 data,addr = sock.recvfrom(1024)
                 print "recived msg",data
                 print "from address is"
                 print addr
      #       n = addr[1] 
             
             elif s == sys.stdin:
                 msg = raw_input('>>>')
                 print msg
                 sock.sendto(msg,(ip,port)) 
               
