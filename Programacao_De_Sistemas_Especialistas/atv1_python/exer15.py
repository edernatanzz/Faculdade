''' 
Faça um programa para a leitura de duas notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e apresentar:
    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.

'''

x = int(input("digite sua primeira nota :"))
y = int(input('Digite sua segunda nota : '))

soma = x+y
media = soma / 2 

def total():
    if x >= 7 :
        print(f'aprovado com media {media}')
    elif x ==10 :
        print(f'Aprovado com Distinção com media {media }')
    elif x <= 7:
        print(f'reprovado com media {media}')
    else : 
        print(f'digite apenas numeros')


total()