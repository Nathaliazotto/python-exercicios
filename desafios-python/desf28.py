#escreva um prog que faca o computador'pensar' em um numero inteiro ente 0 e 5 e peca
#para o usuario tentar descobrir qual foi o numero  escolhido pelo compt

#prog deve escrever na tela se o usuario perdeu ou venceu

from random import randint
from time import sleep
computador=randint(0,5) #faz o computardor pensar
print('--=--' * 10)
print('adivinhe o numero que estou pensando')
print('--=--' * 10)
j=int(input('em que numero eu pensei? ' ))
print('processando...')
sleep(2)
if j==computador:
    print('parabens voce acertou')
else: 
    print('eu ganhei, eu pensei no numero {}'.format(computador))