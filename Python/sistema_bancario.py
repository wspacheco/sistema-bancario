menu =  """

Caro cliente, por favor selecione uma das seguintes opções:

    ------    ##########    ------

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

    ------    ##########    ------

=> """


saldo = 0
limite = 500
extrato = ''
numero_saque = 0
LIMITE_SAQUES = 3


while True:

    operacao = input(menu)
    
    
    if operacao == 'd':
        valor = float(input('Digite um valor para depósito: '))
        
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor: .2f}\n'
                        
        else:
            print('O valor informado é inválido.')


    elif operacao == 's':
        valor = float(input('Digite um valor para saque: '))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saque >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print('Operação não realizada. Você não tem saldo suficiente.')
        
        elif excedeu_limite:
            print('Operação não realizada. Só é permitido sacar até R$ 500.00 por vez.')
            
        elif excedeu_saques:
            print('Operação não realizada. Você excedeu o número máximo de três saques diário.')
    
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor: .2f}\n'
            numero_saque += 1
            
        else:
            print('Operação não realizada. O valor informado é inválido.')


    elif operacao == 'e':
        print('\n=============== EXTRATO ===============')
        print('Não foram realizada movimentações.' if not extrato else extrato)
        print(f'Saldo: R$ {saldo: .2f}')
        print('=======================================')
        

    elif operacao == 'q':
        print('Obrigado por utilizar nossos serviços.')
        break
    
    
    else:
        print('Operação inválida. Por favor selecione uma opção válida.')

