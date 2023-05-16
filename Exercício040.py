n1 = float(input('Informe a primeira nota do aluno: '))
n2 = float(input('Informe a segunda nota do aluno: '))

m = (n1 + n2 ) / 2

if m <5:
    print('O aluno foi reprovado')
elif m <6.9:
    print('O aluno ficará em recuperação')

else:
    print('O aluno foi aprovado')

