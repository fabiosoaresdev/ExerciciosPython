print('-=- ' * 8)
print('Analisador de triângulos V 2.0')
print('-=- ' * 8)
s1 = float(input('Informe o primeiro seguimento: '))
s2 = float(input('Informe o primeiro segundo: '))
s3 = float(input('Informe o primeiro terceiro: '))

if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print('As medidas podem formar um triângulo')
    if s1 == s2 and s2 == s3:
        print('O triangulo é equilátero')
    elif s1 == s2 or s2 == s3:
        print('O triângulo é isóceres')
    else:
        print('O triângulo é escaleno')      
    
else:
    print('As medidas não podem formar um triângulo')
