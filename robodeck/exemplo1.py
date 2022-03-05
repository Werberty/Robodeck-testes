# import numpy as np
from socket import *
from toolbox import *

host = '127.0.0.1'
port = 2000
# 192.168.1.1
# 255.255.255.0

p_id = 1
pid = chr(p_id)
ref = chr(0)
src = [chr(1), chr(68)]
dst = [chr(50), chr(174)]
sid = [chr(0), chr(0)]
act = chr(1)
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
