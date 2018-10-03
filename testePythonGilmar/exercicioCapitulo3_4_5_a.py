frase = input ('Digite uma frase : ')
tamanho = len ( frase )
frasedivtres = int ( tamanho / 3)
primeira = frase [0: frasedivtres ]
segunda = frase [ frasedivtres:frasedivtres*2 ]
terceira = frase [ frasedivtres*2:tamanho ]
print ('primeira: %s\t segunda: %s\t terceira: %s'%(primeira,segunda,terceira))
