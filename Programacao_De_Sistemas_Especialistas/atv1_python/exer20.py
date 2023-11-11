'''
Faça um Programa que pergunte em que turno você estuda. 
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", 
conforme o caso.

'''

x = str(input('digite a inicial do seu turno '))

def saudacoes():
    if x in 'm':
        print(f'bom dia')
    elif x in'v':
        print(f'boa tarde')
    elif x in 'n':
        print(f'boa noite ')
    else :
        print(f'valor invalido !')
        
saudacoes()