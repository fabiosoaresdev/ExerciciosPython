# coletar os valores para realizar os cálculos
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite um segundo valor: '))
n3 = float(input('Digite um terceiro valor: '))

#encontrar o maior valor:
if n1 > n2 and n1 > n3:
    maior = n1   
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
    
#encontrar o menor valor:
if n1 < n2 and n1 < n3:
    menor = n1   
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
    
#printar o resultado final:
print('O maior valor digitado foi {:.0f} e o menor valor digitado foi {:.0f}.'.format(maior, menor))

