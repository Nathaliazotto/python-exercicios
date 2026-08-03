# faca um algoritimo que leia o preco de um produto e mostra seu novo preco com 5% de desconto 

p=float(input('Valor do produto R$: '))
#n=p - (p * 5/100)
d1=0.05
s=p*d1
s1=p-s
print('Seu desconto foi de {:.2f} o valor do seu produto e {:.2f}'.format(s,s1))