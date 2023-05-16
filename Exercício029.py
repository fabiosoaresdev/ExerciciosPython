v = int(input('Informe a velocidade atual do veículo: '))
multa = (v - 80) * 7

if v < 30:
    print('Você está dirigindo devagar, acelere um pouco mais')
    
elif v < 80:
    print('Velocidade ok, tenha um bom dia')
    
elif v == 80:
    print('Você está no limite de velocidade da via, tome cuidado!')
    
else: 
    
    print('Você deverá pagar uma multa equivalente a R${:.2f}'.format(multa))