#Crio os contadores
somaidade = 0
homem = 0
mulher = 0
nomeh = 0

#implemento a estrutura de laço
for p in range(1, 5):
    print(' ----- {}ª PESSOA -----'.format(p))
    nome = input('Nome: ').title().strip()
    sexo = input('Sexo: [M/F]')
    idade = int(input('Idade: '))
    somaidade += idade

    #se a primeira pessoa e o sexo dela forem masculino:
    if p == 1 and sexo in 'Mm':
        homem = idade
        nomeh = nome
    # se sexo for masculino e idade for maior que a variável homem:
    elif sexo in 'Mm' and idade > homem:
        homem = idade
        nomeh = nome
    #Se sexo for feminino e a idade for menor que 20 anos:
    elif sexo in 'Ff' and idade < 20:
        mulher += 1
#Coloquei mediaidade aqui pro programa fazer menas execuções
mediaidade = somaidade / 4

#Área de prints finais
print('A média de idade das pessoas citadas a cima é {}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(homem, nomeh))

if mulher == 1:
    print('{} mulher tem menos de 20 anos'.format(mulher))
else:
    print('{} Mulheres tem menos de 20 anos'.format(mulher))
