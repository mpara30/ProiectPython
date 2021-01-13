import csv

nume_fisier="Date.csv"
fisier_temp="Temperaturi.csv"
fisier_umd="Umiditate.csv"
fisier_viteza="Viteza.csv"
fisier_prezenta="Prezenta.csv"

with open(nume_fisier, 'r', newline='') as csvfile:
    catalog_read = csv.reader(csvfile, delimiter=',',quotechar='!')
   # for row in catalog_read:
      #  with open(fisier_temp, 'a', newline='') as csvfile_temp:
          #  catalog_write_temp = csv.writer(csvfile_temp, delimiter=',',quotechar='!', quoting=csv.QUOTE_MINIMAL)
           # catalog_write_temp.writerow([row[0],row[1],row[2],row[9]])
       # with open(fisier_umd, 'a', newline='') as csvfile_umd:
         #   catalog_write_umd = csv.writer(csvfile_umd, delimiter=',',quotechar='!',quoting=csv.QUOTE_MINIMAL)
           # catalog_write_umd.writerow([row[3],row[4],row[5],row[9]])
       # with open(fisier_viteza, 'a', newline='') as csvfile_viteza:
          #  catalog_write_viteza = csv.writer(csvfile_viteza, delimiter=',',quotechar='!',quoting=csv.QUOTE_MINIMAL)
          #  catalog_write_viteza.writerow([row[6],row[9]])
        #with open(fisier_prezenta, 'a', newline='') as csvfile_prezenta:
           # catalog_write_prezenta = csv.writer(csvfile_prezenta, delimiter=',',quotechar='!',quoting=csv.QUOTE_MINIMAL)
           # catalog_write_prezenta.writerow([row[7],row[8],row[9]])
import pandas
import numpy as np
import matplotlib.pyplot as plt

dt = pandas.read_csv('Temperaturi.csv')

dt.columns = ['Temp 1', 'Temp 2', 'Temp 3', 'Data']

dt['Temp 1'] = dt['Temp 1'].apply(lambda x: (x+5)*4/0.37)
dt['Temp 2'] = dt['Temp 2'].apply(lambda x: (x+5)*4/0.37)
dt['Temp 3'] = dt['Temp 3'].apply(lambda x: (x+5)*4/0.37)

a = np.array(dt['Temp 1'].values.tolist())
dt['Temp 1'] = np.where(a<-5.0, -5.0, a).tolist()

b = np.array(dt['Temp 2'].values.tolist())
dt['Temp 2'] = np.where(b<-5.0, -5.0, b).tolist()

c = np.array(dt['Temp 3'].values.tolist())
dt['Temp 3'] = np.where(c<-5.0, 5.0, c).tolist()

du = pandas.read_csv('Umiditate.csv')

a = np.array(du['Umiditate 1'].values.tolist())
du['Umiditate 1'] = np.where(a>55, 54, a).tolist()

b = np.array(du['Umiditate 2'].values.tolist())
du['Umiditate 2'] = np.where(b>55, 54, b).tolist()

c = np.array(du['Umiditate 3'].values.tolist())
du['Umiditate 3'] = np.where(c>55, 54, c).tolist()

dv = pandas.read_csv('Viteza.csv')

print("1. Listare fisier")
print("2. Listare citiri temperatura+data")
print("3. Listare citiri umiditate+data")
print("4. Listare citiri viteza+data")
print("5. Listare citiri prezenta+data")
print("6. Procesare citiri temperatura+data")
print("7. Procesare citiri umididate+data")
print("8. Procesare citiri viteza+data")
print("9. Salvare valori procesate in fisiere")
print("0. Exit")

x=""

while(x!=0):
    if x == 1:  # Listare fisier Date.csv
        dd = pandas.read_csv('Date.csv')
        print(dd.to_string())
    if x == 2:  # Listare citiri temperatura+data
        d1 = pandas.read_csv('Temperaturi.csv')
        print(d1.to_string())
    if x == 3:  # Listare citiri umiditate+data
        d2 = pandas.read_csv('Umiditate.csv')
        print(d2.to_string())
    if x == 4:  # Listare viteza+data
        d3 = pandas.read_csv('Viteza.csv')
        print(d3.to_string())
    if x == 5:  # Listare prezenta+data
        dp = pandas.read_csv('Prezenta.csv')
        print(dp.to_string())
    if x == 6:  # Procesare citiri temperatura+date
        print(dt.to_string())
        print("Erori:")
        print(dt[dt == -5.0].count())
    if x == 7:  # Procesare citiri umiditat+date
        print(du.to_string())
    if x == 8:  # Procesare citiri viteza+date
        print(dv.to_string())
        print("Media tuturor vitezelor este: ", dv['Viteza 1'].mean())
        print("Viteza 0-10:", dv.iloc[0:10].mean())
        print("Viteza 10-20:", dv.iloc[10:20].mean())
        print("Viteza 20-30:", dv.iloc[20:30].mean())
        print("Viteza 30-40:", dv.iloc[30:40].mean())
        print("Viteza 40-50:", dv.iloc[40:50].mean())
        print("Viteza 50-60:", dv.iloc[50:60].mean())
        print("Viteza 60-70:", dv.iloc[60:70].mean())
        print("Viteza 70-80:", dv.iloc[70:80].mean())
        print("Viteza 80-90:", dv.iloc[80:90].mean())
        print("Viteza 90-100:", dv.iloc[90:100].mean())
    if x == 9:  # Salvare
        dt.to_csv('Temperaturi_modificate.csv')
        du.to_csv('Umiditate_modificate.csv')
        print("Valorile au fost salvate")
    x = int(input("Introduceti comanda dorita:"))
print("La revedere!")

x = []
y = [] #temperatura 1
z = [] #temperatura 2
w = [] #temperatura 3

class grafice_statice ():
    def run(self):
        with open('Temperaturi_modificate.csv.csv', 'r') as csvfile:
            date = csv.reader(csvfile, delimiter= ',')

            for row in date:
                pass
            try:
                y.append(float(row[0]))
                z.append(float(row[1]))
                w.append(float(row[2]))
                x.append(row[3])
            except Exception as e:
                pass
        plt.figure(1)
        plt.plot(x, z, label='Temp 1!')
        plt.plot(x, y, label='Temp 2!')
        plt.plot(x, w, label='Temp 3!')
        plt.xlabel('timp')
        plt.ylabel('temperatura')
        plt.title('temp(timp)')
        plt.legend()
        plt.xticks([0,50,99])



