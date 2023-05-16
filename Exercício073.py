time = 'Palmeiras', 'Corinthians', 'Fluminense', 'Athletico-PR', 'Flamengo', 'Internacional', 'Atlético-MG', 'Bragantino', 'Santos', 'São Paulo'

print('-=-' * 27)
print(f'Os primeiros 3 colocados são: {time[0:3]}\n')
print(F'Os 4 últimos colocados são {time[6:]}\n')

print('ORDEM ALFABÉTICA:')
print(sorted(time))
print(f'\nO Atlético-MG está na {time.index("Atlético-MG")+1}ª posição')
print('-=-' * 27)