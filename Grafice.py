import csv
import matplotlib.pyplot as plt

class grafice_statice():

    def temperaturi():

        a = []
        t1 = []  # temperatura 1
        t2 = []  # temperatura 2
        t3 = []  # temperatura 3

        with open('Temperaturi.csv', 'r') as csvfile: #Se deschide fisierul Temperaturi.csv
            date = csv.reader(csvfile, delimiter=',')
            for row in date:
                pass
                try:
                    t1.append(float(row[0])) #Se ataseaza coloana 1 a temperaturii la grafic
                    t2.append(float(row[1])) #Se ataseaza coloana 2 a temperaturii la grafic
                    t3.append(float(row[2])) #Se ataseaza coloana 3 a temperaturii la grafic
                    a.append(row[3])
                except Exception as e:
                    pass
        plt.figure(1)
        plt.plot(a, t1, color="blue", linewidth=2.5, label='Temperatura 1')  #Se traseaza linia 1 a graficului
        plt.plot(a, t2, color="red", linewidth=2.5, label='Temperatura 2') #Se traseaza linia 2 a graficului
        plt.plot(a, t3, color="green", linewidth=2.5, label='Temperatura 3') #Se traseaza linia 3 a graficului
        plt.xlabel('Timp') #Se denumeste axa x
        plt.ylabel('Temperatura') #Se denumeste axa y
        plt.title('Temperatura in functie de timp') #Titlul graficului
        plt.legend() #Se afiseaza legenda graficului
        plt.xticks([0, 50, 99])
        plt.show() #Se afiseaza graficul

    def umiditate():

        x = []
        u1 = []  # umiditate 1
        u2 = []  # umiditate 2
        u3 = []  # umiditate 3

        with open('Umiditate.csv', 'r') as csvfile: #Se deschide fisierul Umiditate.csv
            date = csv.reader(csvfile, delimiter=',')
            for row in date:
                pass
                try:
                    u1.append(float(row[0])) #Se ataseaza coloana 1 a umiditatii la grafic
                    u2.append(float(row[1])) #Se ataseaza coloana 2 a umiditatii la grafic
                    u3.append(float(row[2])) #Se ataseaza coloana 3 a umiditatii la grafic
                    x.append(row[3])
                except Exception as e:
                    pass
        plt.figure(2)
        plt.plot(x, u1, color="blue", linewidth=2.5, label='Umiditate 1') #Se traseaza linia 1 a graficului
        plt.plot(x, u2, color="red", linewidth=2.5, label='Umiditate 2') #Se traseaza linia 2 a graficului
        plt.plot(x, u3, color="green", linewidth=2.5, label='Umiditate 3') #Se traseaza linia 3 a graficului
        plt.xlabel('Timp') #Se denumeste axa x
        plt.ylabel('Umiditate') #Se denumeste axa y
        plt.title('Graficul umiditatii') #Titlul graficului
        plt.legend() #Se afiseaza legenda graficului
        plt.xticks([0, 50, 99])
        plt.show() #Se afiseaza graficul

    def viteza():

        b = []
        v1 = [] #viteza

        with open('Viteza.csv', 'r') as csvfile: #Se deschide fisierul Viteza.csv
            date = csv.reader(csvfile, delimiter=',')
            for row in date:
                try:
                    v1.append(float(row[0])) #Se ataseaza coloana vitezei la grafic
                    b.append(row[1])
                except Exception as e:
                    pass
        plt.figure(3)
        plt.plot(b, v1,color="red", linewidth=2.5, label='Viteza') #Se traseaza linia 1 a graficului
        plt.xlabel('Timp') #Se denumeste axa x
        plt.ylabel('Viteza') #Se denumeste axa y
        plt.title('Graficul vitezei') #Titlul graficului
        plt.legend() #Se afiseaza legenda graficului
        plt.xticks([0,50,99])
        plt.show() #Se afiseaza graficul

    def prezenta():

        c = []
        p1 = [] #prezenta 1
        p2 = [] #prezenta 2

        with open('Prezenta.csv', 'r') as csvfile: #Se deschide fisierul Prezenta.csv
            date = csv.reader(csvfile, delimiter=',')
            for row in date:
                try:
                    p1.append(float(row[0])) #Se ataseaza coloana 1 a prezentei la grafic
                    p2.append(float(row[1])) #Se ataseaza coloana 2 a prezentei la grafic
                    c.append(row[2])
                except Exception as e:
                    pass
        fig, (ax1, ax2) = plt.subplots(2)
        fig.suptitle('Stacked plots')
        ax1.plot(c, p1, label='Pozitia 1') #Se creeaza primul grafic
        ax2.plot(c, p2, label='Pozitia 2') #Se creeaza al doilea grafic
        plt.xlabel('Timp') #Se denumeste axa x
        plt.ylabel('Pozitie') #Se denumeste axa y
        plt.title('Graficul pozitiei') #Titlul graficului
        plt.legend() #Se afiseaza legenda graficului
        ax1.set_xticks([0, 50, 99])
        ax2.set_xticks([0, 50, 99])
        plt.show() #Se afiseaza graficul







