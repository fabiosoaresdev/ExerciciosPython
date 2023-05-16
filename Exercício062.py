p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = p
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end= '')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer?'))
print(f'Progressão finalizada com {total} termos')
