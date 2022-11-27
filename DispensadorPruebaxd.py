import tkinter as tk
import time
from datetime import datetime
from threading import Thread



MainWindow = tk.Tk()
MainWindow.title("Comedero")
MainWindow.geometry("628x400")
MainWindow.resizable(width=0, height=0)

Hora  = []
Minuto = []
ListaHoras = []
Alimento = 0

estadoLabel = tk.Label(MainWindow, text="Estado: En espera", bg="red", fg="white", width=20, height=4)
estadoLabel.grid(row=0, column=0, sticky=tk.W)
Void = tk.Label(MainWindow, text="", bg="red", fg="white", width=21, height=4)
Void.grid(row=0, column=1, sticky=tk.W)
cantidadLabel = tk.Label(MainWindow, text="", bg="red", fg="white", width=25, height=4)
cantidadLabel.grid(row=0, column=2, sticky=tk.W)
void2= tk.Label(MainWindow, text="").grid(row=1, column=0)
encenderB = tk.Button(MainWindow, text="Encender", command=lambda: Encender(estadoLabel, Void, cantidadLabel), width=20, height=5, borderwidth=3)
encenderB.grid(row=2, column=1)
programarHoraB = tk.Button(MainWindow, text="Programar Hora", command=lambda: programarHora(estadoLabel, Void, cantidadLabel), width=20, height=5, borderwidth=3)
programarHoraB.grid(row=3, column=1)

def programarHora(Estadolabel, void, CantidadLabel):
        ProgamarHora = tk.Toplevel()
        ProgamarHora.title("Programar Hora")
        ProgamarHora.geometry("280x400")
        ProgamarHora.resizable(width=0, height=0)
        HoraLabel = tk.Label(ProgamarHora, text="Hora", font=("arial", 30)).grid(row=0, column=0)
        MinutosLabel = tk.Label(ProgamarHora, text="Minutos", font=("arial", 30)).grid(row=0, column=2)
        ValorHora = tk.StringVar()
        ValorMinutos = tk.StringVar()
        HorasLabel = tk.Label(ProgamarHora, textvariable=ValorHora, font=("Bahnschrift Light", 30), fg="green").grid(row=1, column=0)
        VoidLabel = tk.Label(ProgamarHora, text=":", font=("Bahnschrift Light", 30), fg="green").grid(row=1, column=1)
        MinutosLabel = tk.Label(ProgamarHora, textvariable=ValorMinutos, font=("Bahnschrift Light", 30), fg="green").grid(row=1, column=2)
        HorasScale = tk.Scale(ProgamarHora, from_=0, to=23, orient=tk.HORIZONTAL, command=lambda x: CambiarHora(ValorHora, x)).grid(row=2, column=0)
        MinutosScale = tk.Scale(ProgamarHora, from_=0, to=59, orient=tk.HORIZONTAL, command=lambda x: CambiarMinutos(ValorMinutos, x)).grid(row=2, column=2)
        void = tk.Label(ProgamarHora, text=" ").grid(row=3, column=0)
        AsignarHorasMinutos = tk.Button(ProgamarHora, text="Asignar", command=lambda: Asignar(ValorHora, ValorMinutos, ProgamarHora, Estadolabel, void, CantidadLabel, containerListaHoras))
        AsignarHorasMinutos.grid(row=4, column=0)
        SalirVentana = tk.Button(ProgamarHora, text="Salir", command=ProgamarHora.destroy).grid(row=4, column=2)
        void2 = tk.Label(ProgamarHora, text=" ").grid(row=5, column=0)
        containerListaHoras = tk.Frame(ProgamarHora)
        containerListaHoras.grid(row=8, column=0, columnspan=3)
        label2 = tk.Label(ProgamarHora, text="Lista de Horas", font=("arial", 10))
        label2.grid(row=7, column=0)
        for i in range(len(ListaHoras)):
                label = tk.Label(containerListaHoras, text=ListaHoras[i], font=("arial", 10))
                label.pack()

        labelEliminarTodo = tk.Button(ProgamarHora, text="Eliminar Todo", command=lambda: EliminarTodo(containerListaHoras, ListaHoras))
        labelEliminarTodo.grid(row=7, column=2)
        print(ListaHoras)

        

def Encender(Estadolabel, void, CantidadLabel):
    estadoLabel.config(text="Encendido", bg="green")
    void.config(text=" ", bg="green")
    CantidadLabel.config(text="", bg="green")
    encenderB.config(text="Apagar", command=lambda: Apagar(estadoLabel, Void, cantidadLabel))


def Apagar(Estadolabel, void, CantidadLabel):
    estadoLabel.config(text="Apagado", bg="red")
    void.config(text=" ", bg="red")
    CantidadLabel.config(text="", bg="red")
    encenderB.config(text="Encender", command=lambda: Encender(estadoLabel, Void, cantidadLabel))


def CambiarHora(ValorHora, x):
    ValorHora.set(x)

def CambiarMinutos(ValorMinutos, x):
    ValorMinutos.set(x)

def Asignar(ValorHora, ValorMinutos, ProgamarHora, Estadolabel, void, CantidadLabel, containerListaHoras):
    global Hora, Minuto, Segundos, ListaHoras
    if ValorHora.get() == "" and ValorMinutos.get() == "":
        Hora.append(0)
        Minuto.append(0)
        listaHora = tk.Label(containerListaHoras, width=5, height=1)
        listaHora.pack()
        listaHora.config(text= str(Hora[-1]) + ":" + str(Minuto[-1]) + ":" + str(0))
        ListaHoras.append(str(Hora[-1]) + ":" + str(Minuto[-1]))
    if ValorHora.get() == "" and ValorMinutos.get() != "":
        Minuto.append(ValorMinutos.get())
        Hora.append(0)
        listaHora = tk.Label(containerListaHoras, width=5, height=1)
        listaHora.pack()
        listaHora.config(text= str(Hora[-1]) + ":" + str(Minuto[-1]) + ":" + str(0))
        ListaHoras.append(str(Hora[-1]) + ":" + str(Minuto[-1]))
    if ValorHora.get() != "" and ValorMinutos.get() == "":
        Hora.append(ValorHora.get())
        Minuto.append(0)
        listaHora = tk.Label(containerListaHoras, width=5, height=1)
        listaHora.pack()
        listaHora.config(text= str(Hora[-1]) + ":" + str(Minuto[-1]) + ":" + str(0))
        ListaHoras.append(str(Hora[-1]) + ":" + str(Minuto[-1]))
    if ValorHora.get() != "" and ValorMinutos.get() != "":
        Hora.append(ValorHora.get())
        Minuto.append(ValorMinutos.get())
        listaHora = tk.Label(containerListaHoras, width=5, height=1)
        listaHora.pack()
        listaHora.config(text= str(Hora[-1]) + ":" + str(Minuto[-1]) + ":" + str(0))
        ListaHoras.append(str(Hora[-1]) + ":" + str(Minuto[-1]))

def EliminarTodo(containerListaHoras, ListaHoras):
    global Hora, Minuto, Segundos
    Hora.clear()
    Minuto.clear()
    Segundos.clear()
    ListaHoras.clear()
    for widget in containerListaHoras.winfo_children():
        widget.destroy()


def ComprobarHora(Hora, Minuto, ListaHoras):
    HoraReal = datetime.now().hour
    MinutoReal = datetime.now().minute
    while True:
        for i in range(len(Hora)):
            if HoraReal == int(Hora[i]) and MinutoReal == int(Minuto[i]):
                Encender(estadoLabel, Void, cantidadLabel)
                #Sleep 10 seconds
                time.sleep(10)
                Apagar(estadoLabel, Void, cantidadLabel)
                ListaHoras.pop(i)
                Hora.pop(i)
                Minuto.pop(i)
        else:
            HoraReal = datetime.now().hour
            MinutoReal = datetime.now().minute

Hilo1 = Thread(target=ComprobarHora, args=(Hora, Minuto, ListaHoras))
Hilo1.start()

MainWindow.mainloop()


