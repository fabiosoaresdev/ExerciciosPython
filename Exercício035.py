print('-=- ' * 8)
print('Analisador de triângulos V 1.0')
print('-=- ' * 8)
s1 = float(input('Informe o primeiro seguimento: '))
s2 = float(input('Informe o primeiro segundo: '))
s3 = float(input('Informe o primeiro terceiro: '))

if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print('As medidas podem formar um triângulo')
else:
    print('\033[mAs medidas não podem formar um triângulo')
