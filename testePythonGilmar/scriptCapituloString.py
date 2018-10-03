#frase = input('Digite uma frase:')
#primeiro = frase[0]
#ultimo = frase[-1]
#print ('Primeiro: %s\t Último: %s'%(primeiro,ultimo))

frase1 = 'Eu e minha ^ansia por crescer !'
print ( frase1 . upper ())
frase2 = 'N~ao sei se quero crescer ou ficar na inf^ancia .'
'''
Nas duas linhas abaixo , para calcular o valor
da metade do tamanho da frase , e utilizado a
func~ao len () para calcular o tamanho da frase
ent~ao utilizado o operador / para dividir o
tamanho por 2, a func~ao int () para converter
o resultado para um valor inteiro e ent~ao o
operador + para somar uma unidade ao resultado .
Fique tranquilo caso n~ao tenha entendido
completamente o script abaixo ! Veremos mais
sobre operac~oes matematicas em breve .
Trabalhando com numeros inteiros 11
'''
tamanho = len ( frase2 )
metade = int ( tamanho / 2) + 1
primeira = frase2 [0: metade ]. upper ()
segunda = frase2 [ metade : tamanho ]. lower ()
frase2 = primeira + segunda
print ( frase2 )