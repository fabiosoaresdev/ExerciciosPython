continuar = 'S'
desoito = homem = mulher = 0
while continuar == 'S':
    
    print('-' * 17)
    print('VAMOS CADASTRAR!')
    print('-' * 17)
    idade = int(input('Informe a idade do cliente: '))
    sexo = input('Informe o Sexo do cliente: ').upper().strip()[0]
    
    if idade > 18:
        desoito += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    continuar = input('Deseja continuar?').strip().upper()[0]
    
print(f'{desoito} pessoas tem mais de vinte anos, {homem} pessoas são homens, {mulher} pessoas são mulheres com menos de 20 anos')
    
