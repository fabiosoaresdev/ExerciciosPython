s = input('Informe o sexo: ').upper()[0].strip()
while s not in 'M,F':
    s = input('Informe o sexo: ').upper()[0].strip()
print(f'sexo {s} registrado com sucesso')