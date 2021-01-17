import csv

nume_fisier="Date.csv"
fisier_temp="Temperaturi.csv"
fisier_umd="Umiditate.csv"
fisier_viteza="Viteza.csv"
fisier_prezenta="Prezenta.csv"

with open(nume_fisier, 'r', newline='') as csvfile:
   catalog_read = csv.reader(csvfile, delimiter=',',quotechar='!')
   for row in catalog_read:
      with open(fisier_temp, 'a', newline='') as csvfile_temp:
          catalog_write_temp = csv.writer(csvfile_temp, delimiter=',',quotechar='!', quoting=csv.QUOTE_MINIMAL)
          catalog_write_temp.writerow([row[0],row[1],row[2],row[9]])
      with open(fisier_umd, 'a', newline='') as csvfile_umd:
          catalog_write_umd = csv.writer(csvfile_umd, delimiter=',',quotechar='!',quoting=csv.QUOTE_MINIMAL)
          catalog_write_umd.writerow([row[3],row[4],row[5],row[9]])
      with open(fisier_viteza, 'a', newline='') as csvfile_viteza:
          catalog_write_viteza = csv.writer(csvfile_viteza, delimiter=',',quotechar='!',quoting=csv.QUOTE_MINIMAL)
          catalog_write_viteza.writerow([row[6],row[9]])
      with open(fisier_prezenta, 'a', newline='') as csvfile_prezenta:
          catalog_write_prezenta = csv.writer(csvfile_prezenta, delimiter=',',quotechar='!',quoting=csv.QUOTE_MINIMAL)
          catalog_write_prezenta.writerow([row[7],row[8],row[9]])