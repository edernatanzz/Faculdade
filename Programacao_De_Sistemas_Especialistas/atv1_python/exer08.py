#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês.
x= float(input('qual seu ganho em R$ por hora ? '))
horas = float(input('numero de horas trabalhadas ?'))

salario = x * horas * 30

print(f'seu salario nesse mes foi de R${salario}')