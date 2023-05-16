peso = float(input('Qual o seu peso? \n'))
altura = float(input('Qual a sua altura? \n'))

imc = peso / (altura**2)
print('{:.2f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')