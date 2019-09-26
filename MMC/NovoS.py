# server.py
import socket
import time


def CalcI(peso, altura):
    if (altura <= 2.5):
        imc = round(peso / (altura * altura), 1)

        return imc
    else:
        imc = round(peso * 10000 / (altura * altura), 1)

    return imc
# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machine name
host = socket.gethostname()
port = 9999
# bind to the port
serversocket.bind((host, port))
# queue up to 5 requests
serversocket.listen(5)
while True:
    # establish a connection
    clientsocket, addr = serversocket.accept()
    print("oi")

    entrada = clientsocket.recv(256).decode('ascii').split(' ')

    print(entrada)
    try:
        peso = float(entrada[0])
        altura = float(entrada[1])
        res = str(CalcI(peso, altura))
    except ValueError:
        res = "Entrada invalida"

    print(res)
    clientsocket.send(res.encode('ascii'))
    clientsocket.close()
