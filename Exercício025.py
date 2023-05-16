name = input('Digite seu nome completo: ').title().strip
s = name.find('Santos')

if s == -1:
   print('Você não tem Santos no seu nome')
else:
    print('Você tem Santos no seu nome')