#um professor quer sortear um dos seus quatro alunos para apagar o quadro 
# faca um prog q ajude ele, lendo o nome deles e escreva o nome escolhido

from random import choice
n1=input('primeiro aluno: ')
n2=input('segundo aluno: ')
n3=input('terceiro aluno: ')
n4=input('quarto aluno: ')
l=[n1, n2, n3, n4]
e=choice(l)
print('o aluno escolhido foi {}'.format(e))