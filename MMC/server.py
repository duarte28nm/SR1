# server.py
import socket


# calcular peso
def CalcI(peso, altura):
       if (altura <= 2.5): # altura menor que 2.5m
        imc = round(peso / (altura * altura), 1)

        return imc
    else:
        imc = round(peso * 10000 / (altura * altura), 1)

    return imc

# criar um objeto de soquete
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# obter o nome da máquina local
host = socket.gethostname()
port = 9999

# vincular à porta
serversocket.bind((host, port))

# enfileira até 5 solicitações
serversocket.listen(5)

while True:
    # estabelecer valores
    print(entrada)
    try:
        peso = float(entrada[0])
        altura = float(entrada[1])
        res = str(CalcI(peso, altura))
    except ValueError:
        res = "Entrada invalida"

    # resultado
    print(res)
    clientsocket.send(res.encode('ascii'))
    clientsocket.close()
