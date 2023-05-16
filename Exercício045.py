from random import randint
from time import sleep
#intro do joguinho
print('-=-' * 20)
print('{}                   VAMOS JOGAR JOKENPÔ! {}'.format('\033[32m', '\033[m'))
print('-=-' *20)

#criação da lista do jogo
#pedra == 1
#papel == 2
#tesoura == 3
lista = randint(1,3)

#peço pro user informar em quê ele opção ele quer jogar
op = int(input('Você vai jogar em quê? \033[1;35m PEDRA(1), PAPEL(2) TESOURA (3) \033[m \n'))
print('-=-' *20)
print('{}JO{}'.format('\033[1;31m','\033[m'))
sleep (1)
print('{}KEN{}'.format('\033[1;33m','\033[m'))
sleep (1)
print('{}PÔ!{}'.format('\033[1;32m','\033[m'))

#Montando as regras para empate e vitória:
if op == lista:
    print("DEU EMPATE! Vamos de novo")
    
elif op == 1 and lista == 3:
    print('Você venceu! eu joguei tesoura')
elif op == 2 and lista == 1:
    print('Você venceu! Eu joguei pedra')
elif op == 3 and lista == 2: 
    print('Você venceu! Eu joguei papel')

#Montando as regras para derrota: 
elif op == 3 and lista == 1:
    print('Você perdeu! eu joguei pedra')
elif op == 1 and lista == 2:
    print('Você perdeu! eu joguei papel')
elif op == 2 and lista == 3:
    print('Você perdeu! eu joguei tesoura')
    
else: 
    print('JOGUE DIREITO SEU VAGABUNDO!')