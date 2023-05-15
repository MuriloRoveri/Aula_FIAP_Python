numeros = []
num = 1
negativos = pares = 0
while num != 0:
    print("Digite um numero inteiro")
    num = int(input())
    numeros.append(num)
numeros.pop()
print(f"Tamanho da lista: {len(numeros)}")
numeros.sort()
print(f"Lista em ordem crescente: {numeros}")
for i in numeros :
    if i < 0:
        negativos += 1
    if i > 0 and i % 2 == 0 :
        pares += 1
print(f"Quantidade de numeros negativos: {negativos}")
print(f"Quantidade de numeros positivos: {pares}")