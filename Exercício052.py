n = int(input('Informe um número:'))
tot = 0
for c in range( 1, n+1):
    if n % c == 0:
        print('\033[36m', end='') 
        tot+=1
    else:
        print('\033[33m', end= '')
    print('{}'.format(c), end=' ')
print('\033[mO número {} foi divisível {} vezes'.format(n, tot))
if tot == 2:
    print('O número é primo')
else:
    print('O número não é primo')
    