#prog q pergunte um salario do funcionario e calcule o valor do seu aumento
#para salarios superiores a 1,250 calcule 10% de aumento
#para inferiores ou iguais aumento de 15%

s=int(input('qual seu salario?: '))

if s <=1250:  
    a = s + (s*15/100)
else:
    a = s+ (s*10/100)
print('quem ganhava R${:.2f} seu salario agora e {:.2f}'.format(s,a))