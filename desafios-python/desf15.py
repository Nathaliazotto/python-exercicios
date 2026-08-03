#escreva um prog que pergunte a quantidade de km percorrido por um carro
#alugado e a quantidade de dias pelos quais foi alugado
#calcule o preco a pagar sabendo q o carro custa 60 o dia e 0.15 por km

d=int(input('quantos dias voce alugou o carro?: '))
km=float(input('quantos km percorridos?: '))
pago= (d*60.00) + (km*0.15)
print('O valor que voce precisa pagar e de R${:.2f}'.format(pago))