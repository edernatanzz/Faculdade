'''
Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e 
continue pedindo até que o usuário informe um valor válido.
'''



def nota ():
    while True :
         x = int(input('digite uma sua nota entre 0 a 10 :'))
         if 0 <= x <= 10:
             print(f'a nota digitada foi{x}')
             return 0
         else :
             print('Porfavor Digitar um valor valido')
             
nota()