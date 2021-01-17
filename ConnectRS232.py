import serial

class CnRS232():
    fisier_primit = "Date_RS232.csv" #Se creaza fisierul ce va fi transmis

    ser = serial.Serial(
        port = '/dev/ttyUSB1',
        baudrate = 9600,
        parity = serial.PARITY_ODD,
        stopbits = serial.STOPBITS_TWO,
        bytesize = serial.SEVENBITS
    ) #Deschiderea portului pentru conexiune

    ser.isOpen() #Se porneste conexiunea

