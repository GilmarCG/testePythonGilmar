valorEmprestado = input ('Digite o valor a ser emprestado: ')
valor = float ( valorEmprestado )
numeroParcela = input ('Digite o numero de parcela: ')
parcela = float (numeroParcela)
print ('Digite a opção desejada: ')
print ('1 - Stardard ')
print ('2 - Platinum ')
print ('3 - Gold ')
resposta = input ('')
opcao = int( resposta )
if opcao == 1:
	montante = valor*(1+(2.5/100*parcela))
	prestacao = montante/parcela
elif opcao == 2:
	montante = valor*(1+(1.99/100*parcela))
	prestacao = montante/parcela
elif opcao == 3:
	montante = valor*(1+(1.2/100*parcela))
	prestacao = montante/parcela
else :
	print ('Opçãp invalida !')
print('O montante da divida e: %.2f: , O valor da parcela e: %.2f'%(montante, prestacao))


	


