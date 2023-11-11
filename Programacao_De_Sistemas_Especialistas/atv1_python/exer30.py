'''

Faça um programa que receba dois números inteiros e gere os números
inteiros que estão no intervalo compreendido por eles.

'''

def numbers ():
    
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))

    
    start = min(x, y)
    stop = max(x, y)

    for z in range(start, stop + 1):
        print(f'números inteiros que estão no intervalo compreendido por eles : {z}')
            

numbers()