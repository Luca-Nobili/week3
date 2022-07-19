import socket, platform, os

SRV_ADDR = ""
SRV_PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)
connection, address = s.accept ()

print ("client connected: ", address)

while 1:
	try:
		data = connection.recv(1024)
	except: continue
	if (data.decode('utf-8') == '1'):
		tosend = platform.platform() + " " + platform.machine()
		connection.sendall(tosend.encode())
	elif(data.decode('utf-8') == '2'):
		data = connection.recv (1024)
		try:
			filelist = os.listdir (data.decode('utf-8'))
			tosend = ""
			for x in filelist:
				tosend += "," + x
		except:
			tosend = "Wrong path"
		connection.sendall(tosend.encode())
	elif(data.decode('utf-8') == '0'):
		connection.close()
		connection, address = s.accept()

#Relazione
# prima riga importazione dei moduli per uttilizzare le loro funziomi
# la prima variabile e stata lasciata vuota perche indirizzo ip va inserito dall utente la seconda variabile e assegnata alla porta
# con la variabile s usando la funzione socket.socket specifichiamo che vogliamo usare IPv4 e TCP
# con il bind associamo ip e porta 
# con il listen diciamo quante connessioni simultanee in entrata possiamo avere
# con la funzione  s.accept si utilizza per accettare la connesione 
# secondo input del client il server restituisce delle informazioni
# la variabile data contine i dati che riceviamo, la funzione connection.recv ci fa rivevere i dati dal client 
# nel primo caso restituisce informazioni sul sistema operativo e versione 
# nel secondo caso  ci restituisce i file di una directory specifica
# con il try e l except se ci sara un errore lui ci identifica l errore in modo specifico
# con il terzo caso chiudiamo la connesione
