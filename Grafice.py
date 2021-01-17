import csv
import matplotlib.pyplot as plt

class grafice_statice():

    def temperaturi():

        a = []
        t1 = []  # temperatura 1
        t2 = []  # temperatura 2
        t3 = []  # temperatura 3

        with open('Temperaturi.csv', 'r') as csvfile:
            date = csv.reader(csvfile, delimiter=',')
            for row in date:
                pass
                try:
                    t1.append(float(row[0]))
                    t2.append(float(row[1]))
                    t3.append(float(row[2]))
                    a.append(row[3])
                except Exception as e:
                    pass
        plt.figure(1)
        plt.plot(a, t1, color="blue", linewidth=2.5, label='Temperatura 1')
        plt.plot(a, t2, color="red", linewidth=2.5, label='Temperatura 2')
        plt.plot(a, t3, color="green", linewidth=2.5, label='Temperatura 3')
        plt.xlabel('Timp')
        plt.ylabel('Temperatura')
        plt.title('Temperatura in functie de timp')
        plt.legend()
        plt.xticks([0, 50, 99])
        plt.show()

    def umiditate():

        x = []
        u1 = []  # umiditate 1
        u2 = []  # umiditate 2
        u3 = []  # umiditate 3

        with open('Umiditate.csv', 'r') as csvfile:
            date = csv.reader(csvfile, delimiter=',')
            for row in date:
                pass
                try:
                    u1.append(float(row[0]))
                    u2.append(float(row[1]))
                    u3.append(float(row[2]))
                    x.append(row[3])
                except Exception as e:
                    pass
        plt.figure(2)
        plt.plot(x, u1, color="blue", linewidth=2.5, label='Umd 1')
        plt.plot(x, u2, color="red", linewidth=2.5, label='Umd 2')
        plt.plot(x, u3, color="green", linewidth=2.5, label='Umd 3')
        plt.xlabel('timp')
        plt.ylabel('umiditate')
        plt.title('umiditate(timp)')
        plt.legend()
        plt.xticks([0, 50, 99])
        plt.show()

    def viteza():

        b = []
        v1 = [] #viteza

        with open('Viteza.csv', 'r') as csvfile:
            date = csv.reader(csvfile, delimiter=',')
            for row in date:
                try:
                    v1.append(float(row[0]))
                    b.append(row[1])
                except Exception as e:
                    pass
        plt.figure(3)
        plt.plot(b, v1,color="red", linewidth=2.5, label='Viteza')
        plt.xlabel('Timp')
        plt.ylabel('Viteza')
        plt.title('Viteza in functie de timp')
        plt.xticks([0,50,99])
        plt.show()

    def prezenta():

        c = []
        p1 = []
        p2 = []

        with open('Prezenta.csv', 'r') as csvfile:
            date = csv.reader(csvfile, delimiter=',')
            for row in date:
                try:
                    p1.append(float(row[0]))
                    p2.append(float(row[1]))
                    c.append(row[2])
                except Exception as e:
                    pass
        fig, (ax1, ax2) = plt.subplots(2)
        fig.suptitle('Stacked plots')
        ax1.plot(c, p1, label='Pozitia 1')
        ax2.plot(c, p2, label='Pozitia 2')
        plt.xlabel('Timp')
        plt.ylabel('Pozitie')
        plt.title('pozitie(timp)')
        plt.legend()
        ax1.set_xticks([0, 50, 99])
        ax2.set_xticks([0, 50, 99])
        plt.show()







