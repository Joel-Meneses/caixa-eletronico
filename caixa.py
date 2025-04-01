saldod= [250]
sacado=[0]
depositado=[0]

def deposit(saldod, depositado):
    depositar= input('valor de deposito:')
    if not depositar.isnumeric():
        print("Por favor, digite apenas números!")
    elif float(depositar) <= 0:
        print('sorry,insira um valor positivo para depositar ')

    elif depositar.isnumeric():
        depositado[0] = float(depositar)
        saldod[0]+= depositado[0]
    else:
        print('Algo deu errado, e não sei o porquê')
    

def saque(saldod,sacado):
    sacar= input('valor do saque:')
    if not sacar.isnumeric():
        print("Por favor, digite apenas números!")
    elif float(sacar)<= 0:
        print('porfavor insira um valor positivo para saque')
    elif float(sacar) > saldod[0]:
        print('isso e maior que seu saldo, nao foi possivel sacar,pobre')
    elif sacar.isnumeric():
        sacado[0] = float(sacar)
        saldod[0]-= sacado[0]
    else:
        print('algo deu errado, o problema e voce')
    

def consulta(saldod):
    print(' seu saldo é :{} na conta corrente'.format(saldod[0]))


def extrato(sacar,depositar):
    print('seu extrato...\nvalor sacado: {}\n valor depositado: {}'.format(sacado[0],depositado[0]))
