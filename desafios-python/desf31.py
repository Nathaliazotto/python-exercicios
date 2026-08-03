#um prog pergunte a distancia da sua viagem em km
#calcule o preco da passagem cobrando 0,50 por km para viagens de ate 200km
#0,45 para viagens mais longas 

d=float(input('qual a distancia da sua viagem em Km? '))

if d <=200:
    p=d*0.50
else:
    p=d*0.45
print('A distancia da sua viagem e de {}Km entao o preço da passagem é R$ {:.2f}'.format(d, p))