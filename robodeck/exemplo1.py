import numpy as np
from socket import *
from toolbox import *

host = '127.0.0.1'
port = 2000
# 192.168.1.1
# 255.255.255.0

p_id = 1
pid = np.uint8(p_id)
ref = np.uint8(0)
src = [np.uint8(1), np.uint8(68)]
dst = [np.uint8(50), np.uint8(174)]
sid = [np.uint8(0), np.uint8(0)]
act = np.uint8(1)
cmd, tam = session_open('Eu')
pac = gera_pacote(pid, ref, src, dst, sid, act, tam, cmd)
print(pac)

# print(cmd)
# print(tam)

# cli_sock = socket(AF_INET, SOCK_STREAM)
# cli_sock.connect((host, port))
# msg = input('Digitem um mensagem: ')
# cli_sock.send(msg.encode())
# cli_sock.close()
