#deselvolva um programa que leia as duas notas de um aluno, calcule e mostre sua media

n1=float(input('nota 1: '))
n2=float(input('nota 2: '))
s=(n1+n2)/2
#print('sua media e {:.2f}!'.format(s))
print('media entre {:.2f} e  {:.2f} e igual a  {:.2f}!'.format(n1, n2, s))