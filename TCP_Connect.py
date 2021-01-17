import socket
import csv

class conexiune():

    def functie():
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 9999
        serversocket.bind((host, port))
        serversocket.listen(5)
        return serversocket
    #Se deschide un port pentru a porni conexiunea TCP

    def sendfile(s):
        clientsocket,addr = s.accept()
        print("Conexiune activa",  str(addr))
        with open("Date.csv", 'r', newline='') as csvfile:
            date_read = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in date_read:
                clientsocket.send(str(row).encode('utf-8'))
        #Se distribuie un fisier prin conexiunea TCP

        clientsocket.close() #Se inchide conexiunea

    sendfile(functie()) #Se executa functia de transmitere a fisierului



