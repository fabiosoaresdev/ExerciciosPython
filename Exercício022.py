nome = input('Como é o seu nome completo? ').strip()

print('Seu nome em maiúsculo é: {} '.format(nome.upper()))
print('Seu nome em minúsculo é: {} '.format(nome.lower()))
print('A quantidade de letras ao todo é: {}'.format(len(nome) - (nome.count (' '))))
#print('O primeiro nome tem {} letras'.format(nome.find(' ')))
d = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(d[0], len(d[0])))

