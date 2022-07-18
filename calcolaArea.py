def perimetro():
	print("""
	-Quadrato>>>1
	-Rettangolo >>>2""")

	print('Inserire la scelta: ')
	scelta = int(input(">>> "))
	if scelta == 1:
		print("Hai selezionato il perimetro del Quadrato")
		lato = float(input("Inserisci il valore del lato del quadrato "))
		print("Il perimetro del Quadrato, avente lato", lato, "è:" , lato*4)
	elif scelta == 2:
		print("Hai selezionato il perimetro del Rettangolo")
		base = float(input("Inserisci il valore della base"))
		altezza = float(input("Inserisci il valore dell altezza"))
		print("Il perimetro del rettangolo, avente base" , base, " e altezza",altezza, "è", base*2 + 2*altezza)
	else:
		print("Inserire una scelta valida")
