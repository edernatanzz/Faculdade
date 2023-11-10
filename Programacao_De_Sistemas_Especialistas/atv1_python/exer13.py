#Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.


x = str(input('Digite a inicial do seu sexo '))

if x in 'f':
    print('feminino')
elif x in 'm':
    print('masculino')
else :
    print(' credencial invalida ')