s = float(input('Qual o seu salário?'))
aumento = (s*15)/100
ns = s+ aumento
print('Como você tem sido um bom funcionário na empresa, irei lhe dar um aumento de 15%, agora você receberá R${:.2f}, R${:.2f} a mais que seu salário anterior'.format(ns, aumento))