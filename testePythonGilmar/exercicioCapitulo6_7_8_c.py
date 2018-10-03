valorEmprestado = input ('Digite o valor a ser emprestado: ')
valor = float ( valorEmprestado )
taxaJuro = input ('Digite a taxa de juro: ')
taxa = float (taxaJuro)
numeroParcela = input ('Digite o numero de parcela: ')
parcela = float (numeroParcela)
montante = valor*(1+(taxa/100*parcela))
prestacao = montante/parcela
print('O montante da divida e: %.2f: , O valor da parcela e: %.2f'%(montante, prestacao))

