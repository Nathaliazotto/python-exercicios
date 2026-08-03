#crie um prog que leia quanto de dinheiro uma pessoa tem na carteira e mostre quanos dolares ela poe comprar

d1=float(input('Digite a quantia R$: '))
d2=5.39   #1.00 = 5.39 
s=d1/d2
#s=d1/5.39
print('voce poode comprar {:.2f} dolares!'.format(s))