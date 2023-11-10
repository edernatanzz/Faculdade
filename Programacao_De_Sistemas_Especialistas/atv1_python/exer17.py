#Faça um Programa que leia três números e mostre o maior deles.




x = int(input('Digite um numero :'))
y = int(input('Digite um numero :'))
z = int(input('Digite um numero :'))

def menor_numero():
    if y > x < z:
        print(f'O menor numero foi o Primeiro digitado: {x}')
    elif x > y < z:
        print(f'O menor numero foi o Segundo digitado: {y}')
    elif x < z < y:
        print(f'O menor numero digitado foi o ultimo: {z}')
    else:
        print('Valores iguais')
       
       
def maior_numero():
    if x < y > z :
        print (f' o maior numero foi o segundo digitado : {y}')
    elif y < x > z :
        print (f'o maior numero foi o primeiro digitado {x}')
    elif x < z > y:
        print (f'o maior numero digitado foi o ultimo {z}')
    else :
       print('Valores iguais')
        
menor_numero(),maior_numero()