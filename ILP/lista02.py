def q01():
   # n1,n2,n3,n4 = map(float, input().split())
    n1 = float(input())
    n2= float(input())
    n3 = float(input())
    n4= float(input())
    
    soma = n1+n2+n3+n4
    media = soma /4   
    if media >= 5 :
        print('Parabens bruxao, eh nois que voa, voce passou!')
    else:
        print('Voce nao passou, tente usar a varinha na proxima vez!')
    
def q02():
   # a, b, c = int(input().split())
    quantidade_pista,quantidade_pessoas_pista,quantidade_alunos = map(int, input().split())
    jogar = quantidade_alunos / quantidade_pista
    
    if jogar < quantidade_pessoas_pista : 
        print("S")
    else:
        print('N')
    
    
def q03():
    totalLucas = 0
    totalPedro = 0
    
    for _ in range(3):
        lucas,pedro = map(int,input().split())
        totalLucas += lucas
        totalPedro += pedro
        
    if(totalLucas > totalPedro):
        print("Lucas")
    elif(totalPedro > totalLucas ):
        print('Pedro')
    else:
        print("Empate")
            
def q04():
    x, y = map(int, input().split())
    
    if 0 < x < 100 and 0 < y < 100:
        if x <= 70 and y <= 70:
            print("Coordenada valida e o navio esta perto")
        else:
            print("Coordenada valida e o navio esta longe")
    else:
        print("Coordenada invalida")
        

def q05():
    entrada = map(int(input().split()))
    totalM = entrada / 7
    
    
    
    
            
    
    