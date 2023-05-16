from math import radians, sin, cos, tan

n = float(input('Informe o ângulo que você deseja: '))
seno = sin (radians(n))
coseno = cos(radians(n))
tangente = tan (radians(n))
print('O seno do ângulo {} é {:.2f}'.format(n, seno))
print('O coseno do ângulo {} é {:.2f}'.format(n, coseno))
print('A tangente do ângulo {} é {:.2f}'.format(n, tangente))