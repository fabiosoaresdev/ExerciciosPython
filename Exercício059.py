op = 0
n = 0
n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Informe o segundo número: '))
    
#Início da repetição
while op != 7:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Subtrair
    [4] Dividir
    [5] Maior
    [6] Novos números
    [7] Sair''')
    op = int(input('Informe a sua escolha: '))
    
    #cálculos de soma
    if op == 1:
        r = n1 + n2
        print(f'A soma do número {n1} com o número {n2} é igual a {r}')
    
    #cálculos de multiplicação
    elif op == 2:
        r = n1 * n2
        print(f'{n1} * {n2} é igual a {r}')
    
    #cálculos de divisão
    elif op == 3:
        r = n1 / n2
        resto = n1 // n2
        print(f'{n1} dividido por {n2} é igual a {r:.2f}')
        print(f'O resto da divisão entre {n1} e {n2} é {resto}')
    
    #cálculos de subtração
    elif op == 4:
        r = n1 - n2
        print(f'{n1} menos {n2} é igual a {r:.2f}')
        
        
    #Quem é o maior?
    elif op == 5 and n1 > n2:
        print(f'{n1} é um número maior que{n2}')
    elif op == 5 and n2 < n1:
        print(f'{n1} é menor que {n2}')
    elif op == 5 and n1 == n2:
        print(f'{n1} é igual a {n2}')
        
    elif op == 6:
        n1 = float(input('Informe o primeiro número: '))
        n2 = float(input('Informe o segundo número: '))
        
    elif op == 7:
        break
    
    else: 
        print('Número inválido, por favor, tente novamente!')

        
    