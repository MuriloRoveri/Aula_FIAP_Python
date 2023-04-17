import random
escolha = "sim"
ptojogador = ptopc = 0
while escolha == "sim":
    print("Escolha: \npedra\npapel\ntesoura")
    jog = input()
    sorteio = random.randint(1,3)
    if sorteio == 1:
        pc = "pedra"
    else:
        if sorteio == 2:
            pc = "papel"
        else:
            pc = "tesoura"
    if jog == pc:
        print("Empate\nJogador")