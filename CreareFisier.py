import csv
from os import path

class doc():
    def create(self):
        print(path.exists('Temperaturi.csv')) #Verificarea existentei fisierului

        if path.exists("Temperaturi.csv") == False:

            nume_fisier = "Date.csv" #Fisierul accesat
            fisier_temp = "Temperaturi.csv" #Setarea denumirii pentru fisierul de temperaturi
            fisier_umd = "Umiditate.csv" #Setarea denumirii pentru fisierul de umiditate
            fisier_viteza = "Viteza.csv" #Setarea denumirii pentru fisierul de viteza
            fisier_prezenta = "Prezenta.csv" #Setarea denumirii pentru fisierul de prezenta

            with open(nume_fisier, 'r', newline='') as csvfile:
                catalog_read = csv.reader(csvfile, delimiter=',', quotechar='!') #Se selecteaza si se citesc datele din fisierul csv
                for row in catalog_read:
                    with open(fisier_temp, 'a', newline='') as csvfile_temp:
                        catalog_write_temp = csv.writer(csvfile_temp, delimiter=',', quotechar='!',
                                                        quoting=csv.QUOTE_MINIMAL)
                        catalog_write_temp.writerow([row[0], row[1], row[2], row[9]])
                        #Se scriu citirile despre temperatura si data acestora in noul fisier creat
                    with open(fisier_umd, 'a', newline='') as csvfile_umd:
                        catalog_write_umd = csv.writer(csvfile_umd, delimiter=',', quotechar='!',
                                                       quoting=csv.QUOTE_MINIMAL)
                        catalog_write_umd.writerow([row[3], row[4], row[5], row[9]])
                        # Se scriu citirile despre umiditate si data acestora in noul fisier creat
                    with open(fisier_viteza, 'a', newline='') as csvfile_viteza:
                        catalog_write_viteza = csv.writer(csvfile_viteza, delimiter=',', quotechar='!',
                                                          quoting=csv.QUOTE_MINIMAL)
                        catalog_write_viteza.writerow([row[6], row[9]])
                        # Se scriu citirile despre viteza si data acestora in noul fisier creat
                    with open(fisier_prezenta, 'a', newline='') as csvfile_prezenta:
                        catalog_write_prezenta = csv.writer(csvfile_prezenta, delimiter=',', quotechar='!',
                                                            quoting=csv.QUOTE_MINIMAL)
                        catalog_write_prezenta.writerow([row[7], row[8], row[9]])
                        # Se scriu citirile despre prezenta si data acestora in noul fisier creat

