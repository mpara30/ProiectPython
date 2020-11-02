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

print("Erori:")
print(dt[dt == -5.0].count())
#print(dt)

dt.to_csv('Temperaturi_modificate.csv')

du = pandas.read_csv('Umiditate.csv')
#print(du)

a = np.array(du['Umiditate 1'].values.tolist())
du['Umiditate 1'] = np.where(a>55, 54, a).tolist()

b = np.array(du['Umiditate 2'].values.tolist())
du['Umiditate 2'] = np.where(b>55, 54, b).tolist()

c = np.array(du['Umiditate 3'].values.tolist())
du['Umiditate 3'] = np.where(c>55, 54, c).tolist()

#print(du)

du.to_csv('Umiditate_modificate.csv')

dv = pandas.read_csv('Viteza.csv')

#print(dv)

print("Media tuturor vitezelor este: ",dv['Viteza 1'].mean())

print("Viteza 0-10:",dv.iloc[0:10].mean())
print("Viteza 10-20:",dv.iloc[10:20].mean())
print("Viteza 20-30:",dv.iloc[20:30].mean())
print("Viteza 30-40:",dv.iloc[30:40].mean())
print("Viteza 40-50:",dv.iloc[40:50].mean())
print("Viteza 50-60:",dv.iloc[50:60].mean())
print("Viteza 60-70:",dv.iloc[60:70].mean())
print("Viteza 70-80:",dv.iloc[70:80].mean())
print("Viteza 80-90:",dv.iloc[80:90].mean())
print("Viteza 90-100:",dv.iloc[90:100].mean())

print("1. Listare fisier",
 "2. Listare citiri temperatura+data",
 "3. Listare citiri umiditate+data",
 "4. Listare citiri viteza+data",
 "5. Listare citiri prezenta+data",
 "6. Procesare citiri temperatura+data",
 "7. Procesare citiri umididate+data",
 "8. Procesare citiri viteza+data",
 "9. Salvare valori procesate in fisiere",
 "0. Exit")

x = int(input("Introduceti comanda dorita:"))

if x==1: #Listare fisier Date.csv
    dd = pandas.read_csv('Date.csv')
    print(dd)
if x==2: #Listare citiri temperatura+data
    print(dt)
if x==3: #Listare citiri umiditate+data
    print(du)
if x==4: #Listare viteza+data
    print(dv)
if x==5: #Listare prezenta+data
    dp = pandas.read_csv('Prezenta.csv')
    print(dp)
