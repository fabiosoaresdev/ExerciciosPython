from datetime import date


#Primeiramente, o programa pergunta o ano de nascimento do user
nascimento = int(input('Informe o ano do seu nascimento: '))

#Agora, o programa vai fazer o seguinte cálculo: ano atual - ano de nascimento 
idade = date.today().year

if idade - nascimento  < 18:
    print('{}Ainda não é tempo de se alistar{}'.format('\033[36m', '\033[m'))
    print('Ainda falta {}{}{} ano(s) para você se alistar'.format('\033[36m', 18 - (idade - nascimento), '\033[m'))
    print('O ano de seu alistamento será em {}'.format(nascimento + 18))
    
elif idade - nascimento == 18:
    print('{}está na época de se alistar!{}'.format('\033[32m', '\033[m'))  

else: 
    print('{}Já passou do tempo de se alistar.{}'.format('\033[31m','\033[m'))
    print('Você está a {}{}{} ano(s) atrasado'.format('\033[31m', (18 - (idade - nascimento)) * -1 ,'\033[m'))
    print('O ano de seu alistamento era {}'.format(nascimento + 18))
    
    
#os \033 são as cores 