#faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo
#calcule e mostre o comprimento da hipotenusa

from math import hypot
co=float(input('comprimento do cateto oposto: '))
ca=float(input('comprimento do cateto adjacente: '))
hi=hypot(co,ca)
print('a hip vai medir {:.2f}'.format(hi)) 