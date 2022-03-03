import numpy as np
from socket import *

ip = '127.0.0.1'
port = 2000

# smfe = np.uint8(0x00)
# smfd = np.uint8(0x01)

robodeck = socket(AF_INET, SOCK_STREAM)
robodeck.connect((ip, port))

while 1:
    robodeck.send('msg')
