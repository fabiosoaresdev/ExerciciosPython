preco = float(input('Informe o valor do produto: '))
pag = float(input('''Vamos para o método de pagamento. 
Digite 1 para pagamento a vista 
Digite 2 para Cartão de crédito \n'''))

if pag == 1:
    print('Você receberá 10% de desconto no pagamento, portanto, o novo valor será R${:.2f}'.format(((preco * 10) / 100 - preco) *-1))
    
else: 
    par = input('O pagamento será realizado em quantas parcelas?')
    
    if par == 1: 
        print('Você receberá 5% de desconto, no pagamento, portanto, o novo valor será R${:.2f}'.format(((preco * 5) / 100 - preco)*-1))
    elif par == 2:
        print('O valor do pagamento continuará sendo R${}'.format(preco))
        
    else:
        print('Você receberá 20% de aumento no seu pagamento, o novo valor será R${:.2f}'.format((preco * 20) / 100 + preco))