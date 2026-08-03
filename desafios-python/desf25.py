#ler o nome de uma pessoa e diga se ela tem silva no nome

n=str(input('qual o seu nome? ')).strip()
print('seu nome tem Silva? {}'.format('silva' in n.lower()))
