def maiorNumber():
    a=int(input('digite o numero'))
    b=int(input('digite outro numero'))
    if a > b:
        print('o maior numero é o primeiro' + a)
    elif a == b:
        print ('numeros iguais')
    else :
        print('o segundo numero é o maior' + b)

def q3():
    a = int(input('digite o primeiro numero :'))
    b= int(input('digite o segundo numero :'))

    diferenca = a - b
    if a > b :
        print(a)
        print(diferenca)
    elif a == b:
        print('numeros iguais')
        print('a diferença entre eles é : '+ diferenca) 
    else : 
        print('o maior numero e o segundo : ' + b )
        print('e a diferenca deles é :' + diferenca) 

def q4():
    salario = int(input('o salario é :'))
    valorPrestacao = int(input('valor da prestação : '))
    if valorPrestacao > 20/100:
        print('emprestimo não concedido')
    else:
        print('emprestimo concedido')

def q05():
    av1= int(input('nota 1'))
    av2= int(input('nota 2'))
    av3= int(input('nota 3'))
    total = (av1*1) + (av2*2) + (av3*3)
    media = total / 3

    if media > 60 :
        print('aprovado')
        print(media)
    else:
        print('reprovado')
        print(media)


