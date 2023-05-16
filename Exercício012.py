p = float(input('Qual o valor do produto?'))
d = (p*5)/100
print('Por conta da promoção de 5% em toda a nossa loja, o novo valor do produto é R${:.2f}, e o desconto dele foi de R${:.2f}'.format(p-d, d))