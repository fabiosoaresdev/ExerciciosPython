cont = soma = 0
while True: 
    n = int(input('Digite um número [999 pra parar]'))
    if n == 999:
        break
    soma+=n
    cont += 1
print(f'Você digitou {cont} valores e a soma de todos os números é igual a {soma}')
    