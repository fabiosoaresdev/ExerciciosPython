from random import shuffle
n1 = input('Informe o nome do primeiro aluno: ')
n2 = input('Informe o nome do segundo aluno: ')
n3 = input('Informe o nome do terceiro aluno: ')
n4 = input('Informe o nome do quarto aluno: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem da apresentação será:\n {}'.format(lista))