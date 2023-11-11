'''
Faça um programa que leia 5 números e informe o maior número.

'''

def encontrar_maior():
    maior_numero = float('-inf')  
    
    for i in range(1, 6):
        numero = float(input(f"Digite o {i}º número: "))
        
        if numero > maior_numero:
            maior_numero = numero
    
    print(f"O maior número é: {maior_numero}")


encontrar_maior()
