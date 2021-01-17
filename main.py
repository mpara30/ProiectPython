import Grafice
import TCP_Connect
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
from threading import Thread
#import ConnectRS232

frame=Tk()
frame.title("Grafice")
frame.geometry("400x400")
#Se creaza window-ul cu titlul "Grafice"

def open_file():
    filepath = askopenfilename(
        filetypes=[("CSV File", "*.csv"), ("All Files", "*.*")]
    ) #Se foloseste tkinter pentru a deschide un fisier cvs ales de utilizator
    if not filepath:
        return #Se verifica daca a fost ales un fisier
    text_edit.delete("1.0", tk.END) #Se curata fisierul ales anterior
    with open(filepath, "r") as input_file:
        text = input_file.read() #Deschide si citeste fisierul ales
        text_edit.insert(tk.END, text) #Se atribuie datele citite textbox-ului
    edit.title(f"Alegeti fisierul - {filepath}") #Se seteaza titlul pentru dialogul de selctie a fisierului

edit = tk.Tk()
edit.title("Editare csv")
#Se creaza un nou window cu titlul "Editare csv"
edit.rowconfigure(0, minsize=800, weight=1)
edit.columnconfigure(1, minsize=800, weight=1)
#Se configureaza randurile si coloanele
text_edit = tk.Text(edit)
frame_buttons = tk.Frame(edit)
#Crearea textbox-ului si frame-ului
btn_open = tk.Button(frame_buttons, text="open", command=open_file)
btn_save = tk.Button(frame_buttons, text="save")
#Crearea butoanelor
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
#Salvarea pozitiei butoanelor in grila
frame_buttons.grid(row=0, column=0, sticky="ns")
text_edit.grid(row=0, column=1, sticky="nsew")
#Se creeaza grila pentru frame si textbox


def interfata():
    temperaturi = Button(frame, text="Grafic temperaturi",padx=20, pady=20, activebackground = "#47FF33", command=Grafice.grafice_statice.temperaturi)
    #Se creaza butonul pentru afisarea graficului temperaturii
    temperaturi.pack()
    #Se incarca butonul in interfata grafica
    umiditate = Button(frame, text="Grafic umiditate",padx=20, pady=20, activebackground = "#47FF33", command=Grafice.grafice_statice.umiditate)
    #Se creaza butonul pentru afisarea graficului umiditate
    umiditate.pack()
    # Se incarca butonul in interfata grafica
    viteza = Button(frame, text="Grafic viteza",padx=20, pady=20, activebackground = "#47FF33", command=Grafice.grafice_statice.viteza)
    #Se creaza butonul pentru afisarea graficului vitezei
    viteza.pack()
    # Se incarca butonul in interfata grafica
    prezenta = Button(frame, text="Grafic prezenta",padx=20, activebackground = "#47FF33", pady=20,  command=Grafice.grafice_statice.prezenta)
    #Se creaza butonul pentru afisarea graficului temperaturii
    prezenta.pack()
    # Se incarca butonul in interfata grafica

def tcp():
    TCP_Connect.conexiune.functie()
    TCP_Connect.conexiune.sendfile()

#def rs232():
    #ConnectRS232.CnRS232()

if __name__=='__main__':
    Thread(target = tcp).start() #Porneste firul de executie pentru conexiunea TCP
    Thread(target = interfata).start() #Porneste firul de executie pentru interfata grafica
    ##Thread(target = rs232()).start() #Porneste firul de executie pentru conexiunea prin portul RS232

frame.mainloop()










