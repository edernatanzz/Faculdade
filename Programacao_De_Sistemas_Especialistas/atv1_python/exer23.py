'''
Faça um programa que leia e valide as seguintes informações:
    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';

'''

def program_name():
    while True :
        x = str(input('digite seu nome'))
        if len(x) > 3 :
            print(f'Nome salvo com sucesso : {x}')
            return 0
        else :
            print(' nome muito curto , favor digitar novamente')
            
def program_year():
    while True :
        year = int(input('porfavor digite sua idade'))
        if 0 <= year <= 150:
            print(f'sua idade é de {year}')
            return 0
        else :
            print('numero invalido , por favor digite novamente')
    
program_year()