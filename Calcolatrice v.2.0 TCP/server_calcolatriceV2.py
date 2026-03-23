import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 65432
BUFFER_SIZE = 1024


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:
    sock_server.bind((SERVER_IP, SERVER_PORT))

    #Metti la socket in ascolto per le connessioni in ingresso
    sock_server.listen()

    print(f"Server in ascolto su {SERVER_IP}:{SERVER_PORT}...")

    while True:
        sock_service, address_client = sock_server.accept()
        with sock_service as sock_client:
            # Ricezione dei dati dal client
            dati, addr = sock_client.recvfrom(BUFFER_SIZE)
            dati = dati.decode()
            dati= json.loads(dati)
            primoNumero = dati["primoNumero"]
            operazione = dati["operazione"]
            secondoNumero = dati["secondoNumero"]
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
                
            risposta = {"risultato": risultato}
            print(f"Ricevuto messaggio dal client {sock_client}:{dati}")
            sock_client.sendall(str(risultato).encode())