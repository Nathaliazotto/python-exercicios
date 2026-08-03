#prog leia uma frase e mostre
#quantas vezes aparecem A
#em que posicfao aparece a primeira vez
#em que posicao aperece a ultima vez

f=str(input('digite uma frase: ')).strip().upper().lower()
print('a letra A aparece {} vezes na frase'.format(f.count('a')))
print('a primeira letra A apareceu na posicao {}'.format(f.find('a')+1))
print('a ultima letra A apareceu na posicao {}'.format(f.rfind('a')+1))