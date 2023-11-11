#Faça um Programa que leia três números e mostre-os em ordem decrescente

x = int(input('digite um numero'))
y = int(input('digite outro numero'))
z = int(input('digite o ultimo numero '))

def descrescente():
    print(sorted([x, y, z], reverse=True))
    
descrescente()