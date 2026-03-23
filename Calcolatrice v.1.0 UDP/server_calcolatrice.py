import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 65432
BUFFER_SIZE = 1024

# Creazione del socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:
    sock_server.bind((SERVER_IP, SERVER_PORT)) #Binding della socket alla porta specificata

    #Metti la socket in ascolto per le connessioni in ingresso sock server listen()
    print(f"Server in ascolto su {SERVER_IP}: {SERVER_PORT}...")

    while True:
        # Ricezione dei dati dal client
        sock_service, address_client=sock_server.accept()
        with sock_service as sock_client:
            #Leggi i dati inviati dal client
            dati=sock_client.recv(BUFFER_SIZE).decode()

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

            #Stampa il messaggio ricevuto e invia una risposta al client
            print(f"Ricevuto messaggio dal client {sock_client}: {dati}")
            sock_client.sendall("Messaggio ricevuto dal server".encode())