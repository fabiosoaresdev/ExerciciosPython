cont = 1
media = 0
s = 's'
n = int(input('Informe um número: '))
esc = input('Deseja continuar? {S/N}').lower().strip[0]
soma = maior = menor = n
while esc == s:
    n = int(input('Informe um número: '))
    esc = input('Deseja continuar? {S/N}').lower().strip[0]
    cont += 1
    soma += n
    r = soma / cont
    if n > maior:
        maior = n 
    elif n < menor:
        menor = n 
print(f'Você digitou {cont} valores, a soma deles é igual a {soma}, o maior número é {maior}, o menor é {menor} e a média deles é igual a {r}')
