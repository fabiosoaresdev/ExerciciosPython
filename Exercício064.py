cont = soma = n = 0
n = int(input('Digite um número [999 pra parar]'))
while n != 999:
    soma+=n
    cont += 1
    n = int(input('Digite um número [999 pra parar]'))
print(f'Você digitou {cont} valores e a soma de todos os números é igual a {soma}')
    