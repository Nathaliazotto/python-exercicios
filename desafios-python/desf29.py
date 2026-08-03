#um prog que leia a velocidade de um carro, se ultrapassar 80km mostre mensagem de multado
#multa vai custar 7,oo por cada km acima do limite

p=int(input('Qual a velocida voce percorreu? '))
if p <=80:
    print('voce esta na velocidade adequada, PARABENS!')
else:
    c=p-80
    c1=c*7.0
    print('sua velocidade e {}'.format(p))
    print('sua velocidade esta {}km' ' acima da media, multa de R${:.2f} '.format(c,c1))