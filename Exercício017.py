from math import hypot

x = float(input('Qual o comprimento do cateto oposto? '))
y = float(input('Qual o comprimento do cateto adjacente? '))
print('A hipotenusa é equivalente a {:.2f}'.format(hypot(x, y)))
