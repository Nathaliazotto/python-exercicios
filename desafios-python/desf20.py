# o mesmo professor quer sortear a ordem de apresentacoes de trab
#faca um prog que leia o nome dos quatro e mostre a ordem sorteada

from random import shuffle
n1=input('primeiro aluno: ')
n2=input('segundo aluno: ')
n3=input('terceiro aluno: ')
n4=input('quarto aluno: ')
l=[n1, n2, n3, n4]
shuffle(l)
print('a ordem de apresentacao sera ')
print(l)