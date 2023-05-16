frase = input('Digite uma frase: ').upper().strip()
print('A frase tem {} letras A'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {} e a última letra A apareceu na posição {}. '.format(frase.find('A')+1, frase.rfind('A')+1))
