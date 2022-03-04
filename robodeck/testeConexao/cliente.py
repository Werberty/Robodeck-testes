# import numpy as np
from socket import *

host = '127.0.0.1'
port = 2000
# 192.168.1.1
# 255.255.255.0

# smfe = np.uint8(0x00)
# smfd = np.uint8(0x01)

cli_sock = socket(AF_INET, SOCK_STREAM)
cli_sock.connect((host, port))
msg = input('Digitem um mensagem: ')
cli_sock.send(msg.encode())
cli_sock.close()
