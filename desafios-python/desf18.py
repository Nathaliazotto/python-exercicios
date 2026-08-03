#faca um prog q leia um angulo qualquer e mostre na tela o valor do seno cosseno e tangente do angulo

from math import radians, sin, cos, tan
angulo=float(input('digite o angulo que vc deseja: '))
seno=sin (radians(angulo))
print('o angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno=cos (radians(angulo))
print('o angulo de {} tem o COSSENO de{:.2f}'.format(angulo, cosseno))
tangente=tan (radians(angulo))
print('o angulo {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))