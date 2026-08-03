#prog q leia nome completo de uma pessoa e mostre em seguida
#primeiro e o ultimo nome separadamenente

n=str(input('qual seu nome completo? ')).strip()
nome= n.split()
print('seu primeiro nome e {}'.format(nome[0]))
print('seu ultimo nome e {}'.format(nome[len(nome)-1]))
'''print(n.find(" "))
print(n.rfind(" "))'''