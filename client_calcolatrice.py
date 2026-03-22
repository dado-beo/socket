import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

# Creazione del socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Dati input
primoNumero = float(input("Inserisci il primo numero: "))
operazione = input("Inserisci l'operazione (simbolo): ")
secondoNumero = float(input("Inserisci il secondo numero: "))

messaggio = {"primoNumero": primoNumero,
    "operazione": operazione,
    "secondoNumero": secondoNumero}

messaggio_json = json.dumps(messaggio)
sock.sendto(messaggio_json.encode("utf-8"), (SERVER_IP, SERVER_PORT))

# Risposta dal server
data, addr = sock.recvfrom(BUFFER_SIZE)
risposta = json.loads(data.decode("utf-8"))

print(f"Messaggio ricevuto dal server {addr}: {risposta['risultato']}")

# Chiusura del socket
sock.close()