import socket
import struct
import binascii

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.htons(0x0800)) #creating socket

while True:

    s.bind((Your_IP,PORT))
    packet = s.recvfrom(2048)

    ethernet_header = packet[0][0:14] #Get Ethernet Header

    eth_header = struct.unpack("!6s6s2s", ethernet_header)

    print("Destination MAC:" + binascii.hexlify(eth_header[0]) + 
        "Source MAC:" + binascii.hexlify(eth_header[1]) + 
        "Type:" + binascii.hexlify(eth_header[2]))
    
    ipheader = packet[0][14:34]
    ip_header = struct.unpack("!12s4s4s", ipheader)
    print ("Source IP:" + socket.inet_ntoa(ip_header[1]) + 
           "Destination IP:" + socket.inet_ntoa(ip_header[2]))