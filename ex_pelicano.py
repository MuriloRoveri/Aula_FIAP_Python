#Exercício Soma do comprimento da asa do pelicano utilizando "while"
asas = 1
somatoria = 0

while asas != 0:
    print("Digite um comprimento de asa:")
    asas = float(input())
    somatoria += asas
    #somatoria = somatoria + asas
print(f"O Total do comprimento das asas é {somatoria}")