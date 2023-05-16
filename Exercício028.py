from random import randint # O randint é responsável por escolher um número aleatório na lista a ser criada
from time import sleep # usei pra dar um charme...

print('-=-' * 16)
pc = randint(0,5)
print('Vou pensar em um número de 0 a 5! Tente advinhar') #O computador começa a "pensar"
print('-=-' * 16)


n = int(input('Você acha que eu pensei em qual número?\n')) # O jogador informa um número

print ('PROCESSANDO...')
sleep(3) # o programa para por uns 3 segundos antes de exibir o resultado

if n == pc:
    print('=' * 40)
    print('Você acertou! eu realmente pensei no número {}'.format(pc))
    print('=' * 40)
else:
    print('=' * 33)
    print('Você errou seu otário! Eu pensei no número {} kkkkkkkkkkk'.format(pc))
    print('=' * 33)