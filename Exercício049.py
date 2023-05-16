n = int(input('Informe um número:'))
print ('-=-' * 20)
print(' ' *18,'Tabuada do número: ',n)
print ('-=-' * 20)
for c in range(0 , 11):
    print('{} * {} = {}'.format(n, c, c*n))
    