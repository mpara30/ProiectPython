
import Grafice
import threading
import time
import TCP_Connect
from tkinter import *
from tkinter import filedialog

frame=Tk()
frame.title("Proiect Python")
frame.geometry("400x400")

def file_opener():
    input = filedialog.askopenfile(initialdir="/")
    print(input)
    for i in input:
        print(i)

def tcp():
    print("conexiune")
    TCP_Connect.conexiune()
    time.sleep(1)

def interfata():
    selectare = Button(frame, text="Selectati un fisier csv", padx=20, pady=20, command=lambda:file_opener())
    selectare.pack()
    temperaturi = Button(frame, text="Grafic temperaturi",padx=20, pady=20, command=Grafice.grafice_statice.temperaturi)
    temperaturi.pack()
    umiditate = Button(frame, text="Grafic umiditate",padx=20, pady=20, command=Grafice.grafice_statice.prezenta)
    umiditate.pack()
    viteza = Button(frame, text="Grafic viteza",padx=20, pady=20, command=Grafice.grafice_statice.viteza)
    viteza.pack()
    prezenta = Button(frame, text="Grafic prezenta",padx=20, pady=20,  command=Grafice.grafice_statice.prezenta)
    prezenta.pack()

threads = []
for i in range(1):
    y = threading.Thread(target = tcp)
    z = threading.Thread(target = interfata)
    y.start()
    z.start()

frame.mainloop()










