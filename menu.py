from caixa import *

usuario=str(input("ola,digite seu nome:"))
inserir= int(input('digite sua senha:'))
senha= 1221
def menu():

    print('seja bem vindo {} oque voce deseja realizar?'.format(usuario))
    r = int(input('digite 1 para consultar seu saldo;\ndigite 2 para depositar;\ndigite 3 para sacar;\n digite 4 para ver extrato\ninsira:'))
    if r==1:
        consulta(saldod)
        
    elif r==2:
        deposit(saldod,depositado)
       
    elif r==3:
        saque(saldod,sacado)

    elif r==4:
        extrato(sacado,depositado)
        
    else:
        print('opcao inexistente, escolha as opcoes')
    menu()

if inserir == senha:
    menu()
else:
    print('Senha incorreta, ladrão')

