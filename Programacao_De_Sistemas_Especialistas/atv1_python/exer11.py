#Faça um Programa que peça dois números e imprima o maior deles.

x= int(input('Digite um Numero : '))
y= int(input('Digite outro numero : '))

def maior():
    if x < y :
        print(f'o maior numero digitado foi o Segundo : {y}')
    else :
        print(f'o maior numero digitado foi o primeiro : {x}')
    
maior()