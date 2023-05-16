# O randint é responsável por escolher um número aleatório na lista a ser criada
from random import randint 
contador = 0

print('-=-' * 16)
pc = randint(0,10)
#O computador começa a "pensar"
print('Vou pensar em um número de 0 a 10! Tente advinhar') 
print('-=-' * 16)
 # O jogador informa um número
n = int(input('Você acha que eu pensei em qual número?\n'))

while n != pc:
    contador += 1
    if n < pc:
        print('Mais... Tente mais uma vez')
        n = int(input('Você acha que eu pensei em qual número?\n'))
    else:
        print('Menos... Tente mais uma vez')
        n = int(input('Você acha que eu pensei em qual número?\n'))

if n == pc and contador == 1:
    print('=' * 40)
    print(f'Você acertou de primeira! eu realmente pensei no número {pc}')
    print('=' * 40)
else:
    print('=' * 60)
    print(f'Você acertou depois de {contador} tentativas! eu realmente pensei no número {pc}')
    print('=' * 60)
