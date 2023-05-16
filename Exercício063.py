n = int(input('Informe quantos termos você deseja mostrar '))

cont = 3
n0 = 0
n1 = 1
print(f'{n0} -> {n1} ->', end='')

while cont <= n:
    n2 = n0+n1
    n0 = n1; n1 = n2
    cont += 1
    print(f'{n2} ->', end= '')
print(' fim')