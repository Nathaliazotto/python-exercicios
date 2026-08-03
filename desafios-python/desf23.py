#um prog que leia um numero de 0 a 9999 e mostre cada um dos digitos separados

num=int(input('digite um numero? '))
u=num // 1%10
d=num // 10%10
c=num // 100%100
m=num //1000%1000
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))