#Faça um Programa que peça a temperatura em graus Fahrenheit, 
#transforme e mostre a temperatura em graus Celsius.

x = float(input('digite seu graus Fahrenheit'))

c = 5 * ((x-32) / 9)

print(f'a temperatura {x} Fahrenheit convertida para celsius é igual a : {c}')