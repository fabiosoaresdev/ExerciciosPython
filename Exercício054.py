from datetime import date
maior = 0
menor = 0
atual = date.today().year
for c in range(1,8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('{} pessoas são de maior'.format(maior))
print('{} pessoas são de menor'.format(menor))