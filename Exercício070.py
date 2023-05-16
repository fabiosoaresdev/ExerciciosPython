continuar = 'S'
soma = mil = barato = cont = 0

while continuar == 'S':
    produto = input('Informe o nome do produto: ')
    preço = float(input('Informe o valor do produto: '))
    cont += 1
    soma += preço
    
    if preço > 1000:
        mil += 1

    if cont == 1:
        barato = preço
    elif preço < barato:
        barato = preço
        
    continuar = input('Deseja continuar? ').upper().strip()
print(f'Seu gasto total foi {soma}, {mil} produtos custaram mais de R$1000,00 e o produto mais barato foi {barato}')