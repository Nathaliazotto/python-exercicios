#faca um prog que leia a largura e altura de um parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, 
# sabendo que cada litro de tinta, pinta uma area de 2m2 
A=float(input('Digite a Altura da parede: '))
L=float(input('Digite a Largura da parede: '))
s=A*L
print('A Area da sua parede e {}'.format(s))
s1=s/2
print("Você precisará de {:.2f} litros de tinta".format(s1))