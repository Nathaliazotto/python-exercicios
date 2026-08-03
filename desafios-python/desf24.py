#um prog que leia o nome da cidade e diga se ela comeca ou n com o nome SANTO

p=str(input('qual o nome da sua cidade? ')).strip()
print(p[:5].upper() == 'SANTO')
#print(p.split()[0])
#print(p.find('santo')) 