v = float(input('Informe a distância da sua viagem em quilômetros: '))

if v <= 200:
    print('Sua viagem irá custar R${:.2f}'.format(v * 0.50))
else:
    print('Sua viagem irá custar R${:.2f}'.format(v * 0.45))
print('Tenha um bom dia!')