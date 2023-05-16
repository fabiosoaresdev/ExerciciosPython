maior = 0
menor = 0
for p in range(1, 7):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    
    if p == 1:
        maior = peso
        menor = peso
    
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('A pessoa mais pesada tem {}KG e a mais leve tem {}KG'.format(maior, menor))
        