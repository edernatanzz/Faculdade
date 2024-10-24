def q01():
    tabuada = int(input("Tabuada do número: "))
    for count in range(10):
        print(f"{tabuada} x {count + 1} = {tabuada * (count + 1)}")

def q01While():
    while True:
        print('Informe o número entre 1-10 para geração da tabuada:')
        numeroEscolhido = int(input())
        if 1 <= numeroEscolhido <= 10:
            break
        else:
            print('Número inválido. Tente novamente.')

    print('Informe o número para início da tabuada:')
    numeroInicio = int(input())
    print('Informe o número para fim da tabuada:')
    numeroFim = int(input())

    if numeroInicio < numeroFim:
        for i in range(numeroInicio, numeroFim + 1):
            print(f"{numeroEscolhido} * {i} = {numeroEscolhido * i}")
    else:
        print('O número de início deve ser menor que o número de fim.')


def q02():
    while True:
        print('Informe o número entre 1-10 para geração da tabuada:')
        numeroEscolhido = int(input())
        if 1 <= numeroEscolhido <= 10:
            break
        else:
            print('Número inválido. Tente novamente.')

    print('Informe o número para início da tabuada:')
    numeroInicio = int(input())
    print('Informe o número para fim da tabuada:')
    numeroFim = int(input())

    if numeroInicio < numeroFim:
        for i in range(numeroInicio, numeroFim + 1):
            print(f"{numeroEscolhido} * {i} = {numeroEscolhido * i}")
    else:
        print('O número de início deve ser menor que o número de fim.')

def q03():
    while True :
        print('informe o numero para tabela')
        numeroEscolhido = int(input())
        if 1 <= numeroEscolhido <= 10:
            break 
        else : print('invalido')
        print('informe o numero para inicio da tabuada')
        numeroInicio = int(input())
        print('informe o numero para o fim da tabuada:')
        numeroFim = int(input())
        if numeroInicio < numeroFim:
                for i in range(10):
                    if(i%2==0):
                        print(i, "Números pares!")
        
        
def q05():
    