# Dessecador de variável #

algo=input('Digite algo: ')

print( 'O que você digitou é uma variável do tipo: ', type(algo))

print('Só tem espaço?', algo.isspace())
print('O que você digitou é um número? ', algo.isnumeric())
print('O que você digitou é uma palavra?', algo.isalpha())
print('O que você digitou é alfa numérico?', algo.isalnum())
print('Está MAIÚSCULO?', algo.isupper())
print('Está minúsculo?', algo.islower())
print('Está capitalizada?', algo.istitle())


