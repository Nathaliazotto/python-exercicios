#crie um prog que leia o nome completo de uma pessoa
#nome all maiusculo
#all minusculp
#quantas letras tem
#quantas letras tem 1 nome 

p=str(input('qual seu nome completo? ')).strip()
print('seu nome em MAIUSCULO e {}'.format(p.upper()))
print('seu nome em minusculo e{}'.format(p.lower()))
print('seu nome tem ao todo {}'.format(len(p.replace(" ", ""))))
print('seu primeiro nome tem {} letras'.format(p.find(" ")))
