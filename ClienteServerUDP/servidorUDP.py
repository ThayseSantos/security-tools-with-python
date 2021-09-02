import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket criado com sucesso!!!")

host = 'localhost'
porta = 5432

# LIGAÇÃO ENTRE CLIENTE-SERVIDOR
s.bind((host, porta))
mensagem = "\nServidor: Olá Cliente, tudo bem!?"

while 1:
    dados, endereco = s.recvfrom(4096) #4096 bytes através do objeto de conexão (s)

    if dados:
        print("Servidor enviando mensagem...")
        s.sendto(dados + (mensagem.encode()), endereco)
