numeros = []
num = 1
pares = 0

while num != 0:
    num = int(input("\nDigite um numero inteiro: "))
    numeros.append(num)
    if num % 2 == 0:
        print(f"O Número {num} é par")
    else:
        print(f"O Número {num} é ímpar")
    print("Digite \"0\" para encerrar\n")
    print("-" * 30)