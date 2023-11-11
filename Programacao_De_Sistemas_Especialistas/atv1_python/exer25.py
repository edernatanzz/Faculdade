'''
Supondo que a população de um país A seja da ordem de 80000 habitantes 
com uma taxa anual de crescimento de 3% e que a população de B seja 200000 
habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule 
e escreva o número de anos necessários para que a população do país A ultrapasse ou 
iguale a população do país B, mantidas as taxas de crescimento.
'''

a = float(input('populaçao pais A'))
b = float(input('populacao pais b'))
taixa_anual1= float(input('taxa de crescimento'))
taixa_anual2 = float(input('taxa de crescimeto'))

anos = 0

while a < b :
    a += a*taixa_anual1
    b += b*taixa_anual2
    anos += 1 

print (f'Número de anos necessários: {anos}')