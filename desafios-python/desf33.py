#um prog que leia 3 numeros e mostre qual o maior e qual o menor

n=int(input('digite 1 numero: '))
n2=int(input('digite 2 numero: '))
n3=int(input('digite 3 numero: '))

menor=n
if n2<n and n2<n3:
    menor=n2
if n3<n and n3<n2:
    menor=n3

maior=n
if n2>n and n2>n3:
    maior=n2
if n3>n and n3>n2:
    maior=n3
print('o menor valor digitado foi {}'.format(menor))
print('o maior valor digitado foi {}'.format(maior))
