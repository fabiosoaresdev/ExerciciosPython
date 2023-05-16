f = input('Digite uma frase: ').strip().upper().split()
j = ''.join(f)
i= j[::-1]
'''for l in range (len(j) -1, -1, -1):
    i+= (j[l])'''
print('O inverso de {} é {}'.format(j, i))
if i == j:

    print('A frase é um palíndromo')
    
else:
    print('A frase não é um palíndromo')