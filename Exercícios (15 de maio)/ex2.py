#import statistics
numeros = []
num = media = 0.0
soma = 0.0
for i in range(0, 20, 1):
    print("Digite um numero real")
    num = float(input())
    numeros.append(num)
for i in numeros:
    soma += 1
    media = soma / len(numeros)
    print(f"Média dos valores é {media}")