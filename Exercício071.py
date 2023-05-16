print('-=' * 12)
print('{}BANCO FABIAUM 24 HORAS{}'.format('\033[1;33m','\033[m'))
print('-=' * 12)
dinheiro = float(input('Informe quanto você deseja sacar: '))
ced = 200
totced = 0
total = dinheiro
while True: 
    if total >= ced:
        total -= ced
        totced += 1
        
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de {ced}')
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        totced = 0
        if total == 0:
            break

