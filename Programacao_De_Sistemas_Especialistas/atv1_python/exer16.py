#Faça um Programa que leia três números e mostre o maior deles.

x = int(input('Digite um numero :'))
y = int(input('Digite um numero :'))
z = int(input('Digite um numero :'))

def maior_numero():
    if x < y > z :
        print (f' o maior numero foi o segundo digitado : {y}')
    elif y < x > z :
        print (f'o maior numero foi o primeiro digitado {x}')
    elif x < z > y:
        print (f'o maior numero digitado foi o ultimo {z}')
    else :
       print('Valores iguais')
        
maior_numero()