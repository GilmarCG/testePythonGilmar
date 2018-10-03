digAltura = input('Digite a Altura: ')
altura = float (digAltura)
digPeso = input('Digito o Peso: ')
peso = float (digPeso)
imc = peso / (altura**2)		
if (imc < 18.5):
	print (' Abaixo do peso ')
elif ( 18.5<=imc and imc < 25):
	print(' Peso normal ')
elif (25<=imc and imc < 30): 
	print(' sobrepeso ')
elif (30<=imc and imc < 35):
	print(' Obesidade grau I ')
elif (35<=imc and imc < 40): 
	print(' Obesidade de grau II ')
else:
	print(' Obesidade de grau II ')
		