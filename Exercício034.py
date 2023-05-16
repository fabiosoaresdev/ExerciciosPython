s = float(input('Informe o valor do seu salário atual: '))

if s <= 1250:
    print('Já que você recebia o valor de R${:.2f}, seu novo salário irá valer {:.2f}'.format(s, (s*15) / 100 + s))
else:
    print('Já que você recebia o valor de R${:.2f}, o seu novo salário irá valer {:.2f}'.format(s, (s*10) / 100 + s))
    