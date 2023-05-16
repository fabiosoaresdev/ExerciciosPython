lista = ('Lápis', '1.75', 'Borracha', '2.00', 'Caderno', '15.90', 'Estojo', '25.00', 'Compasso', '9.99', 'Mochila Nike', '140,87','Canetas', '22,30',  'Livros', '99,98')

print('-'*38)
print(f'{"MATERIAIS ESCOLARES":^38}')
print('-'*38)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>6}')