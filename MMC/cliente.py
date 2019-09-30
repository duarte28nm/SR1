# client.py
import socket
from tkinter import *


def enviar():
    # criar um objeto de soquete
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # obter o nome da máquina local
    host = socket.gethostname()
    port = 9999

    # conexão com o nome do host na porta
    s.connect((host, port))
    print("Conexão estabelecida")

    # peso, altura e resposta
    peso = str(ptxt.get())
    altura = str(atxt.get())
    s.send((peso + " " + altura).encode('ascii'))
    l = str(s.recv(256).decode('ascii'))
    label.configure(text="Resultado = " + l)

    # resposta
    try:
        if (float(l) < 18.5):
            a = Label(window, text="você está abaixo do peso.")
            a.grid(column=0, row=7)
        elif (float(l) >= 18.5 and float(l) < 24.9):
            a = Label(window, text="você está no peso ideal.")
            a.grid(column=0, row=7)
        elif (float(l) >= 25 and float(l) < 29.9):
            a = Label(window, text="você está com sobrepeso")
            a.grid(column=0, row=7)
        elif (float(l) < 34.9 and float(l) >= 30):
            a = Label(window, text="você está acima do peso. Obesidade Grau 1.")
            a.grid(column=0, row=7)
        elif (float(l) < 39.9 and float(l) >= 35):
            a = Label(window, text="você está acima do peso. Obesidade Grau 2.")
            a.grid(column=0, row=7)
        elif (float(l) >= 40):
            a = Label(window, text="você está acima do peso. Obesidade Grau 3.")
            a.grid(column=0, row=7)
    except ValueError:
        a = Label(window, text="Erro na classificação")
        a.grid(column=0, row=7)

    s.close()

    # Botões de entrada
window = Tk()
window.geometry("450x300")
window.title("Cálcular IMC")

Lab1 = Label(window, text='Digite seu peso:', font=('Arial', 11))
Lab1.grid(column=0, row=0)

ptxt = Entry(window, width=4)
ptxt.grid(column=1, row=0)

Lab2 = Label(window, text='Digite sua altura:', font=('Arial', 11))
Lab2.grid(column=0, row=1)

atxt = Entry(window, width=4)
atxt.grid(column=1, row=1)

RBTN1 = Button(window, text="Calcular seu IMC", command=enviar)
RBTN1.grid(column=0, row=3)

label = Label(window, text="")
label.grid(column=0, row=5)

window.mainloop()



