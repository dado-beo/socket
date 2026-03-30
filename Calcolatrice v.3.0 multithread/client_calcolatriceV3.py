import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
    sock_service.connect((SERVER_IP, SERVER_PORT))
    
    # Dati input
    primoNumero = float(input("Inserisci il primo numero: "))
    operazione = input("Inserisci l'operazione (simbolo): ")
    secondoNumero = float(input("Inserisci il secondo numero: "))

    # Dizionario
    messaggio = {
        "primoNumero": primoNumero,
        "operazione": operazione,
        "secondoNumero": secondoNumero
    }

    # Trasformazione in JSON e invio dei dati
    messaggio_json = json.dumps(messaggio)
    sock_service.sendall(messaggio_json.encode("utf-8"))
    data = sock_service.recv(1024) # il parametro indica la dimensione massima dei dati che possono essere ricevuti in una sola volta

# a questo punto la socket è stata chiusa automaticamente
print("Ricevuto", data.decode())