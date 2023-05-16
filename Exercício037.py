n = int(input('Informe um número: '))
print('Você deseja realizar a conversão para que tipo numérico?')
con = int(input('{ 1 } BINÁRIO \n{ 2 } OCTAL \n{ 3 } HEXADECIMAL\n'))

if con == 1:
    print('O valor {} convertido para BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
elif con == 2:
    print('O valor {} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif con == 3:
    print('O valor {} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('{} POR GENTILEZA, DIGITE OS NÚMEROS DE 1 A 3{}'.format('\033[1;31m', '\033[m'))