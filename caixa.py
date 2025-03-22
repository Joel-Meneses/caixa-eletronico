saldod= [250]
usuario=str(input("Ola,digite seu nome:"))
sacado=[0]
depositado=[0]

def deposit(saldod, depositado):
    depositar= input('Valor de deposito:')
    if not depositar.isnumeric():
        print("Por favor, digite apenas números!")
    elif float(depositar) <= 0:
        print('Sorry,insira um valor positivo para depositar ')

    elif depositar.isnumeric():
        depositado[0] = float(depositar)
        saldod[0]+= depositado[0]
    else:
        print('Algo deu errado, e não sei o porquê')
    

def saque(saldod,sacado):
    sacar= input('Valor do saque:')
    if not sacar.isnumeric():
        print("Por favor, digite apenas números!")
    elif float(sacar)<= 0:
        print('Porfavor insira um valor positivo para saque')
    elif float(sacar) > saldod[0]:
        print('Isso e maior que seu saldo, nao foi possivel sacar,pobre')
    elif sacar.isnumeric():
        sacado[0] = float(sacar)
        saldod[0]-= sacado[0]
    else:
        print('algo deu errado, o problema e voce')
    
    
def consulta(saldod):
    print(' Seu saldo e {} na conta corrente'.format(saldod[0]))

def extrato(sacar,depositar):
    print('Seu extrato...\nvalor sacado{}\n valor depositado{}'.format(sacado,depositado))


def menu():
    print('Seja bem vindo {} oque voce deseja realizar?'.format(usuario))
    global saldod
    r = int(input('Digite 1 para consultar seu saldo;\ndigite 2 para depositar;\ndigite 3 para sacar;\n digite 4 para ver extrato\ninsira:'))
    if r==1:
        consulta(saldod)
        

    elif r==2:
        deposit(saldod,depositado)
       


    elif r==3:
        saque(saldod,sacado)

    elif r==4:
        extrato(sacado,depositado)
        
    
    else:
        print('Opção inexistente, escolha as opcoes')

    menu()

menu()


