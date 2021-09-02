import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    except socket.error as e:
        print("A conexão falhou!!!")
        print("Erro: {}".format(e))
        sys.exit()

    print("Socket criado com sucesso")

    # DEFINIR HOST E PORTA ALVO:
    hostalvo = input("Digite o Host ou IP a ser conectado: ")
    portaalvo = input("Digite a porta a ser conectada: ")

    # TENTAR CONEXÃO:
    try:
        s.connect((hostalvo, int(portaalvo)))
        print("Cliente TCP conectado com sucesso no Host: " + hostalvo + " e na Porta: " + portaalvo + "!")
        # Finalizar conexão depois de 2 segundos (sem looping)
        s.shutdown(2)

        # Caso der erro de conexão:
    except socket.error as e:
        print("Não foi possível conetar no Host: " + hostalvo + "  - Porta: " + portaalvo)
        print("Erro: {}".format(e))
        sys.exit()


if __name__ == '__main__':
    main()
