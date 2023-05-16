# Início do mundo 2

#O programa começa pedindo os dados do cliente para o empréstimo
casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
ano = float(input('Em quantos anos você pagará esse empréstimo? '))
prestacao = casa / (ano * 12)
minimo = (salario * 30) / 100

# A mensalidade a ser paga não pode ser mais que 30% do salário do cliente, então o seguinte cálculo será realizado: 
# CASA / MES < SALARIO * 30 / 100
if prestacao <= minimo:
    print('Para adquirir a casa, as prestações serão de {}R${:.2f} {} portanto, parece uma boa realizar o investimento.'.format('\033[1;32m',prestacao, '\033[m'))
else:
    print('Para financiar uma casa de {} você precisará pagar prestações de R${:.2f} e isso é mais que 30% do seu salário'.format(casa, minimo))
    print('Portanto, o seu direito a financiamento foi {}NEGADO{}'.format('\033[1;31m', '\033[m'))


