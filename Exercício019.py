from time import sleep
from random import choice

n1 = input('Informe o nome do primeiro aluno: ')
n2 = input('Informe o nome do segundo aluno: ')
n3 = input('Informe o nome do terceiro aluno: ')
n4 = input('Informe o nome do quarto aluno: ')
n5 = input('Informe o nome do quinto aluno: ')
n6 = input('Informe o nome do sexto aluno: ')

lista = [n1, n2, n3, n4,n5,n6]

x = choice(lista)
print(f'O aluno(a) escolhido(a) foi {n1}')

sleep(90)
