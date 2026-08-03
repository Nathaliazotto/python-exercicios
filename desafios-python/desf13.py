#faca um algoritimo que leia o salario de uma pessoa e mostra seu novo salario com 15% de aumento

s=int(input('Digite seu salario: '))
#n= s + (s * 15/100)
a=1.15 #0.15 e para saber o valor que aumenta somando o total mais o salario
c=s*a
print('Seu salario agora e {:.2f}'.format(c))