#faca um prog que leia um ano qualquer e mostre se ele e bisseexto

a=int(input('qual o ano? '))
if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
        print('{} é um ano bissexto'.format(a))
else:
        print('{} não é um ano bissexto'.format(a))
