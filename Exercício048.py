# primeiro criei contadores
soma = 0
cont = 0
#Depois criei o laço de repetição
for c in range (1, 501,2):
    #se o resto da divisão de c e 3 for igual a 0, o contador soma vai contar soma (0) + C
    # já o contador cont, vai somar cont (0) + 1, ou seja, toda vez que o programa captar um número, o cont vai receber +1
    if c % 3 == 0:
        soma += c
        cont += 1
#Print dos resultados
print('A soma de todos os {} valores é igual a: {}'.format(cont, soma))
