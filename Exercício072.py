n = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Desesseis', 'Desessete', 'Desoito', 'Desenove', 'Vinte'

numero = int(input('Informe um número entre 0 e 20: '))
while numero < 0 or numero > 20:
    print('Você digitou um valor errado, por favor, tente novamente')
    numero = int(input('Informe um número entre 0 e 20: '))
print(f'O número que você digitou foi {n[numero]}')
    

