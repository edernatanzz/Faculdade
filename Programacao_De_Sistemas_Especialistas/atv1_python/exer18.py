#Faça um programa que pergunte o preço de três produtos e 
# informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

x = float(input('valor do produto 1 '))
y = float(input('valor do produto 2 '))
z = float(input('valor do produto 3 '))

def menor_produto():
    if y > x < z :
        print(f'o produto mais barato foi o primeiro de R${x}')
    elif x> y <z :
        print(f'o produto mais barato foi o segundo de R${y}')
    elif x > z < y:
        print(f'o produto mais barato foi o terceiro de R${z}')
    else :
        print(f'os produtos tem valores iguais')

menor_produto()