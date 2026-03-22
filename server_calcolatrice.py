import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

# Creazione del socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((SERVER_IP, SERVER_PORT))

print("Server in attesa di messaggi...")

while True:
    # Ricezione dei dati dal client
    data, addr = sock.recvfrom(BUFFER_SIZE)
    dati_json = json.loads(data.decode("utf-8"))
    
    primoNumero = dati_json["primoNumero"]
    operazione = dati_json["operazione"]
    secondoNumero = dati_json["secondoNumero"]
    
    print(f"Messaggio ricevuto dal client {addr}: {data.decode()}")
    
    # Calcolo
    risultato = 0
    if operazione == '+':
        risultato = primoNumero + secondoNumero
    elif operazione == '-':
        risultato = primoNumero - secondoNumero
    elif operazione == '*':
        risultato = primoNumero * secondoNumero
    elif operazione == '/':
        risultato = primoNumero / secondoNumero
        
    # Risposta in JSON
    risposta = {"risultato": risultato}
    risposta_json = json.dumps(risposta)
    sock.sendto(risposta_json.encode("utf-8"), addr)