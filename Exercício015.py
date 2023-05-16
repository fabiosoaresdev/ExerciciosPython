d = float(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos KM você rodou com o carro?'))

dd = d * 60
dkm = km * 0.15


print('Tendo em vista que você ficou {:.0f} dias com o carro e rodou {}KM, o valor a ser pago é de R${:.2f}'.format(d, km, dd+dkm))