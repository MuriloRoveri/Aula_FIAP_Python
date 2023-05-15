def divisao(n1, n2):
    result = n1%n2
    return result

print("Digite dois números inteiros para serem divididos:")
num1 = int(input())
num2 = int(input())
resultado = divisao(num1, num2)
print(f"O Resto da divisão é {resultado}")