# client.py
import socket
from tkinter import *


def enviar():
    # criar um objeto de soquete
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # obter o nome da máquina local
    host = socket.gethostname()
    port = 9999
    # connection to hostname on the port

    s.connect((host, port))
    print("Conexão estabelecida")

    peso = str(txt.get())
    altura = str(txt2.get())
    s.send((peso + " " + altura).encode('ascii'))
    lol = str(s.recv(256).decode('ascii'))
    label.configure(text="Resultado = " + lol)

    try:
        if (float(lol) < 18.5):
            a = Label(window, text="você está abaixo do peso.")
            a.grid(column=0, row=7)
        elif (float(lol) >= 18.5 and float(lol) < 24.9):
            a = Label(window, text="você está no peso ideal.")
            a.grid(column=0, row=7)
        elif (float(lol) >= 25 and float(lol) < 29.9):
            a = Label(window, text="você está com sobrepeso")
            a.grid(column=0, row=7)
        elif (float(lol) < 34.9 and float(lol) >= 30):
            a = Label(window, text="você está acima do peso. Obesidade Grau 1.")
            a.grid(column=0, row=7)
        elif (float(lol) < 39.9 and float(lol) >= 35):
            a = Label(window, text="você está acima do peso. Obesidade Grau 2.")
            a.grid(column=0, row=7)
        elif (float(lol) >= 40):
            a = Label(window, text="você está acima do peso. Obesidade Grau 3.")
            a.grid(column=0, row=7)
    except ValueError:
        a = Label(window, text="Erro na classificação")
        a.grid(column=0, row=7)

    s.close()


window = Tk()
window.geometry("250x100")
window.title("Cálculo IMC")

Lab1 = Label(window, text='Digite seu peso:', font=('Arial', 11))
Lab1.grid(column=0, row=0)

txt = Entry(window, width=4)
txt.grid(column=1, row=0)

Lab2 = Label(window, text='Digite sua altura:', font=('Arial', 11))
Lab2.grid(column=0, row=1)

txt2 = Entry(window, width=4)
txt2.grid(column=1, row=1)

RBTN1 = Button(window, text="Calcular seu IMC", command=enviar)
RBTN1.grid(column=0, row=3)

label = Label(window, text="")
label.grid(column=0, row=5)

window.mainloop()


