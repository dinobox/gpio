from socket import socket, AF_INET, SOCK_DGRAM
def send(msg,addr,port):
    s = socket(AF_INET, SOCK_DGRAM)
    s.sendto(msg, (addr, port))
    re_msg, addr = s.recvfrom(500)
    print re_msg
send('21_on','localhost',3000)
