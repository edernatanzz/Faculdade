#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

x = str(input('Digite um letra :'))

if x in ['a','e','i','o', 'u']:
    print('Vogal')
elif x in ['1','2','3','4','5','6','7','8','9'] : 
    print('Porfavor Digite apenas Letras')
else :
    ('Consoante')