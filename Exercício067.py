while True:
    n = int(input('Informe um número:'))
    if n < 0:
        break
    print ('-=-' * 20)
    print(' ' *18,'Tabuada do número: ',n)
    print ('-=-' * 20)
    for c in range (0, 11):
        print(f'{n} * {c} = {n*c}')
    