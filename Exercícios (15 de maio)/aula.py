#Funções
# def nome_da_função (parâmetros):
#     <corpo da função>
#     return "valor de retorno"
# Parâmetros podem existir ou não
# corpo da função -> onde é realizado a sequência de instruções
# return -> retornar informações

# EXEMPLO 1
def frase1() :
    print("Hello World")

def frase2() :
    return "Hello World"

frase1()
texto = frase2()
print(texto)


# EXEMPLO 2
def soma (n1, n2) :
    result = n1 + n2
    return result

print("Digite 2 números inteiros")
num1 = int(input())
num2 = int(input())
resultado = soma(num1, num2)
print(f"A soma é: {resultado}")


# EXEMPLO 3
def situacao(estado) :
    if estado.lower() == "solteiro" :
        print("Você é solteiro")
    else :
        print("Você é casado")

print("Digite seu estado civil")
ecivil = input()
situacao(ecivil)