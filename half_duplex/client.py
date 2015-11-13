import socket
port = 5000
ip = '127.0.0.1'
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
     print "enter the msg"
     msg = raw_input(">>>")
     sock.sendto(msg,(ip,port))   
     data,addr = sock.recvfrom(1024)
     print "recived msg",data
     print "from address is "
     print addr   
