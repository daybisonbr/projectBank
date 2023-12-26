##TIPOS DE OPERAÇÕES
##DEPOSITO
##SAQUE
##TRANSFERENCIA
##LIMITE DE 3 SAQUES DIARIOS MAX: 500
##EXTRATO DEVE SER EXIBIDO O SALDO ATUAL DA CONTA R$

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)
    response = opcao.lower()
    
    if response == 'd':
        input_valor = float(input("Qual valor deseja depositar? "));
        if input_valor > 0 :
            saldo += input_valor;
            extrato += f"Deposito de R$ {input_valor:.2f} \n";
            print(f"Você despositou R$ {input_valor:.2f}, Saldo atual da conta é R$ {saldo:.2f}");
            
    elif response == 's':
        input_valor_saque = float(input("Qual valor deseja Sacar? "))
        if input_valor_saque > saldo:
            print("Você não possui saldo suficiente para finalizar essa transação")
        if input_valor_saque > 500:
            print("Não é possivel fazer saques maiores que R$ 500,00")
        else:
            if input_valor_saque <= saldo:
                if LIMITE_SAQUE <= 0:
                    print("Não é possivel fazer o saque, Limite de saque diario foi alcançado.")
                else:
                    saldo -= input_valor_saque
                    LIMITE_SAQUE -= 1
                    print(f"Saque efetuado com sucesso. Saldo atual da conta é R$ {saldo:.2f}")
                    extrato += f"Saque de R$ {input_valor_saque:.2f} \n"

    elif response == 'e':
        print("\n ====================== EXTRATO ======================")
        print("Não foram realizadas movimentações." if not extrato else f"Extrado: \n{extrato}")
        print(f"Saldo: R$ {saldo:.2f}")
        print("=====================================================")
    elif response == 'q':
        break
    else:
        print("Operação invalida, por favor selecione novamente a opção desejada.")
