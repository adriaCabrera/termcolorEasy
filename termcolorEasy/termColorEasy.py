class termcolorEasy:
	def instructions():
		print("Instrucciones: COLOR FORMATO TEXTO")
		print("Instructions: COLOR FORMAT TEXT")
	def write(texto):
		from termcolor import colored

		def recorrido(inici, conjunto):
			cadena = ""
			for element in range(inici, len(conjunto)):
				cadena += conjunto[element]+" "
			return(cadena)

		listado = texto.split(" ")
		if len(listado) > 1:
			try:
				cadena = recorrido(2,listado)
				print(colored(cadena, listado[0], attrs=[listado[1]]))
			except KeyError:
				try:
					cadena = recorrido(1,listado)
					print(colored(cadena, listado[0]))
				except KeyError:
					try:
						cadena = recorrido(1,listado)
						print(colored(cadena, attrs=[listado[0]]))
					except KeyError:
						print(colored("INVALID COLOR! NEED VALID COLOR ARGUMENT", attrs=["bold"]))
		else:
			try:
				print(colored(texto))
			except KeyError:
				print(colored("INVALID VALUE! NEED COLOR ARGUMENT", attrs=["bold"]))
			
termcolorEasy.write("blue bold aaaa")
