from socket import *

host = '127.0.0.1'
port = 2000

serv_sock = socket(AF_INET, SOCK_STREAM)
serv_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serv_sock.bind((host, port))
serv_sock.listen(5)
# Aguardando conexão
con, cliente = serv_sock.accept()
# Conectado e aguardando mensagem
recebe = con.recv(1024)
# Recebe mensagem
print(f'Mensagem recebida: {recebe}')
serv_sock.close()