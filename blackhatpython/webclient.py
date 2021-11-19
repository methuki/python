#! /usr/bin/python2

import socket

target_host = "punki.blackwalnut.trail"
target_port = 443

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host,target_port))
client.send("GET / HTTP/1.1\r\nHost: punki.blackwalnut.trail\r\n\r\n")

response = client.recv(4096)
print(response)
