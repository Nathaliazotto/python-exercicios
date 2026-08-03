#prog que leia o numero inteiro e mostre na tela se ele e par ou impar
n=int(input('digite um numero: '))
r=n%2
if r==0:
    print('o numero {} e PAR'.format(n))

else:
    print('o numero {} e IMPAR'.format(n))
