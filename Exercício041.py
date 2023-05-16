from datetime import date

ano = int(input('Digite o ano de nascimento do atleta: '))

idade = date.today().year

if idade - ano <=9:
    print('Atleta mirim')
elif idade - ano <= 14:
    print('Atleta Infantil')
elif idade - ano <= 19:
    print('Atleta Júnior')
elif idade - ano <=22:
    print('Atleta Senior')
elif idade - ano > 22:
    print('Atleta master')
