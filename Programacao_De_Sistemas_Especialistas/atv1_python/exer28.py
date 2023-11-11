'''
Faça um programa que leia 5 números e informe a soma e a média dos números.

'''

def numeros ():
    soma = 0
    for i in range(1, 6):
        numero = float(input(f"Digite o {i}º número: "))
        soma += numero 
    media = soma / i 
    print(media)
        

numeros()


    
    
    