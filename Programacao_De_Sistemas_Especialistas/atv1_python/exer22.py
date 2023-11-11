'''
Faça um programa que leia um nome de usuário
e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.

'''
x = str(input('Qual seu nome '))

def senha ():
    while True :
        y = str(input('Digite sua senha :'))
        if y ==x :
            print('Senha igual ao nome , por favor digite novamente')
        else :
            print(f'usuario {x} e senha : {y} cadastros com sucesso!.')
            return 0
        
senha()