i = int(input("Digite o valor de i entre 1 a 3: "))
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if i < 0:
    i *= -1

if i == 1:
    if a > b > c:
        print(f"A ordem crescente é: {c} {b} {a}")
    if a > c > b:
        print(f"A ordem crescente é: {b} {c} {a}")
    if b > a > c:
        print(f"A ordem crescente é: {c} {a} {b}")
    if b > c > a:
        print(f"A ordem crescente é: {a} {c} {b}")
    if c > a > b:
        print(f"A ordem crescente é: {b} {a} {c}")
    if c > b > a:
        print(f"A ordem crescente é: {a} {b} {c}")

elif i == 2:
    if a > b > c:
        print(f"A ordem decrescente é: {a} {b} {c}")
    if a > c > b:
        print(f"A ordem decrescente é: {a} {c} {b}")
    if b > a > c:
        print(f"A ordem decrescente é: {b} {a} {c}")
    if b > c > a:
        print(f"A ordem decrescente é: {b} {c} {a}")
    if c > a > b:
        print(f"A ordem decrescente é: {c} {a} {b}")
    if c > b > a:
        print(f"A ordem decrescente é: {c} {b} {a}")

elif i == 3:
    if a > b > c:
        print(f"{b} {a} {c}")
    if a > c > b:
        print(f"{c} {a} {b}")
    if b > a > c:
        print(f"{a} {b} {c}")
    if b > c > a:
        print(f"{c} {b} {a}")
    if c > a > b:
        print(f"{a} {c} {b}")
    if c > b > a:
        print(f"{b} {c} {a}")    

elif i > 3:
    print("O Valor de i não é nenhum dos 3 escolhidos.")