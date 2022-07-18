def perimetro():
	scelta=-1
	while(scelta != 0):
	     
		print("Il programma calcola il perimetro di una fugura geometrica")
		print("""
		-Quadrato >>1
		-Rettangolo >>2
		-Cerchio >>3
		-Triangolo Equilatero >>4
		-Premere 5 per uscire""")
	
		print('Inserisci la scelta: ')
		scelta = int(input(">>> "))

		if scelta == 1:
			print("Hai selezionato il perimetro del Quadrato")
			lato = float(input("Inserisci il valore del lato del Quadrato "))
			print("Il perimetro del Quadrato, avente lato", lato, "è:" , lato*4)
		elif scelta == 2:
			print("Hai selezionato il perimetro del Rettangolo")
			base = float(input("Inserisci il valore della base"))
			altezza = float(input("Inserisci il valore dell altezza"))
			print("Il perimetro del Rettangolo, avente base", base, " e altezza",altezza, "è: " ,base*2 + 2*altezza)
		elif scelta == 3:
			print("Hai selezionato il perimetro del cerchio")
			TT=3.14
			raggio = float(input("Inserisci il valore del raggio"))
			print("Il perimero del Cerchio, avente raggio", raggio, "è:" ,raggio **2 * TT)
		elif scelta == 4:
			print("Hai selezionato il perimetro del triangolo equilatero")
			latotriangolo= float(input("Inserisci il valore del lato del triangolo"))
			print("Il valore del perimetro del triangolo, avente lato", latotriangolo, "è: " , latotriangolo*3)
		elif scelta == 5:
			print("Arrivederci")
			return 0
		else:
			print ("Inserire una scelta valida") 

perimetro();


#relazione
#programma per calcolo del perimetro di diverse forme geometriche
#alla fine di ogni calcolo riparte il menu grazie al ciclo while cosi facendo il programma non esce in automatico
#alla fine di ogni calcolo
#aggiunta di un elif per permettere all utente di gestire l' uscita dal programma dopo aver finito le sue operazioni
#per quanto riguarda il perimetro del cerchio ho aggiunto la variabile pigreco visto che il suo valore non cambia mai
#essendo una costante per il calcolo del perimetro del cerchio 
#l'uso del float permette all'utente di inserire numeri decimali
