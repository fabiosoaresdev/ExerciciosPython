# A biblioteca randon vai ser responsável por fazer o pc pensar em um número
from random import randint 
# Esse novo = S é pra dar um tranco no programa e fazer ele rodar inicialmente, o por quê você verá depois
novo = 'S'
# Enquanto a variável novo for igual a S:
while novo == 'S':
    v = 0
    while True:
        pc = randint(0, 10)
        player = int(input('Escolha um número entre 0 e 10: '))
        soma = pc + player 
        # O usuário escolhe um número e o pc também
        
        # O usuário escolhe um tipo (par ou ímpar e o pc escolhe também)
        tipo = input('Par ou Impar?').upper().strip()[0]
        while tipo not in 'PI':
            print('Informe os dados de maneira correta!')
            tipo = input('Par ou Impar?').upper().strip()[0]
        
        # Aqui eu criei as regras do jogo
        if tipo == 'P':
            if soma % 2 == 0:
                print('Você venceu!')
                v += 1
            else:
                print('EU GANHEI!')
                break
        if tipo == 'I':
            if soma % 2 != 0:
                print('Você venceu!')
                v += 1
            else: 
                print(' EU GANHEI!')
                break
                
        #Considerações finais com resultados 
        print(f' Você jogou {player}, eu joguei {pc}, logo, a soma é: {soma}')
    print('Você acertou por {}{}{} vezes consecutivas!'.format('\033[1;33m', v, '\033[m'))
    
    # A variável novo vai entrar em cena agora pra fazer o jogo ser resetado caso o player queira jogar novamente 
    novo = input('Vamos jogar de novo? [S/N]').upper().strip()
    