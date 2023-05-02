# Inicia as variaveis e vetores
ids=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
senhas=[1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999, 0000]
SaldoContas=[2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000]
cedulas50=100
cedulas10=100
cedulas05=100
cedulas01=100
CedulasTotal = 6600
reset=3


while reset!=2:
    print("\n============================ CYBER BANK ===================================")

    # Faz a conferencia da senha.
    id = int(input("Informe o seu ID: "))
    for i in range(10):
        if ids[i]==id:
            confSenha = senhas[i]

    senha = int(input("Informe sua SENHA: "))

    while confSenha != senha:
        print("SENHA INCORRETA\n")
        senha = int(input("Informe sua SENHA novamente: "))
    print("SENHA CORRETA\n")

    # mostra saldo do usuário.
    for i in range(10):
     if ids[i]==id:
         SaldoAtual = SaldoContas[i]
    print("Seu saldo atual é de:", SaldoAtual,"B$\n")

    # Pergunta para o usuário o valor que ele deseja sacar, se não tiver saldo o programa informa e pede para informar um novo saque.
    ValorSaque = float(input("Informe o valor que você deseja sacar: "))
    while ValorSaque > SaldoAtual:
        print("Saldo insuficiente.")
        ValorSaque = float(input("Informe o valor que você deseja sacar novamente: "))
    #Não aceita saque acima de 1000B$.
    while ValorSaque > 1000:
        print("Não é permitido saque acima de 1000B$.")
        ValorSaque = float(input("Informe o valor que você deseja sacar novamente: "))

    #Não aceita sacar acima do valor total da máquina.
    while ValorSaque > CedulasTotal:
        print("Saldo Insuficiente na máquina. Restam ",CedulasTotal,"B$\n")
        print("Deseja realizar outro saque?")
        opçao = int(input("1 - Sim ou 2 - Não: "))

        if(opçao == 1):
            ValorSaque = float(input("Informe o valor que deseja sacar: "))
        else:
            print("Sessão Finalizada.")
            print("Até Breve!")
            exit()

    #Se o usuário sacar 0 bits, o programa finaliza.
    if (ValorSaque==0):
        print("Sessão Finalizada.")
        print("Até Breve!")
        exit()

    # baixa o saldo do usuário.
    for i in range(10):
        if ids[i]==id:
            NovoSaldo = SaldoAtual-ValorSaque
            SaldoContas[i]=int(NovoSaldo)

    NovoTotal = CedulasTotal-ValorSaque
    CedulasTotal=int(NovoTotal)

    # Faz a contagem das notas de 50
    cinquenta = int(ValorSaque / 50)
    ValorSaque = ValorSaque % 50
    Notas50 = 0
    Sobras = 0

    for i in range(cinquenta):
        cedulas50 = cedulas50 - 1
        if cedulas50 >= 0:
            Notas50 = Notas50 + 1
        else:
            Sobras = Sobras + 1

    ValorSaque = ValorSaque + (Sobras * 50)

    # Faz as contagens das notas de 10
    dez = int(ValorSaque / 10)
    ValorSaque = ValorSaque % 10
    Notas10 = 0
    Sobras = 0

    for i in range(dez):
        cedulas10 = cedulas10 - 1
        if cedulas10 >= 0:
            Notas10 = Notas10 + 1
        else:
            Sobras = Sobras + 1

    ValorSaque = ValorSaque + (Sobras * 10)

    # Faz as contagens das notas de 05
    cinco = int(ValorSaque / 5)
    ValorSaque = ValorSaque % 5
    Notas05 = 0
    Sobras = 0

    for i in range(cinco):
        cedulas05 = cedulas05 - 1
        if cedulas05 >= 0:
            Notas05 = Notas05 + 1
        else:
            Sobras = Sobras + 1

    ValorSaque = ValorSaque + (Sobras * 5)

    # faz as contagens das notas de 01
    um = int(ValorSaque / 1)
    ValorSaque = ValorSaque % 1
    Notas01 = 0
    Sobras = 0

    for i in range(um):
        cedulas01 = cedulas01 - 1
        if cedulas01 >= 0:
            Notas01 = Notas01 + 1
        else:
            Sobras = Sobras + 1


    # Dá a opção das cedulas ao usuário.
    print('Notas R$ 50,00 = ', Notas50)
    print('Notas R$ 10,00 = ', Notas10)
    print('Notas R$  5,00 = ', Notas05)
    print('Notas R$  1,00 = ', Notas01)