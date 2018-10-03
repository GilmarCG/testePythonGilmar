digProva = input ('Digite a nota da 1° Prova: ')
prova1 = float( digProva )
digProva = input ('Digite a nota da 2° Prova: ')
prova2 = float( digProva )
digProva = input ('Digite a nota da 3° Prova: ')
prova3 = float( digProva )
digProva = input ('Digite a nota da 4° Prova: ')
prova4 = float( digProva )
media = (prova1 + prova2 + prova3 + prova4)/4
if  (media >= 7):
	print ('Aprovado.')
elif (media >=5 and media <7):
	print ('Recuperação.')
else:
	print ('reprovado.')
	
	


