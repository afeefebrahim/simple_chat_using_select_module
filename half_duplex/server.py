import socket
port = 5000
ip = '127.0.0.1'
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((ip,port))
while True:
     data,addr = sock.recvfrom(1024)
     print "recived msg",data 
     print "from address is " 
     print addr
     msg = raw_input(">>>")
     print msg 
     sock.sendto(msg,(ip,addr[1])) 
