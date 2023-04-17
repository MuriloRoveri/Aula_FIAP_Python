valor_pagar = int(input("Digite o valor a ser pago R$ "))
valor_pago = int(input("Digite o valor efetivamente pago R$ "))

if valor_pagar > valor_pago:
    troco = valor_pagar - valor_pago
    print("\nVocê ainda deve R$", troco)

elif valor_pagar < valor_pago:
        troco = valor_pago - valor_pagar
        print("\nVocê vai receber de troco R$", troco)
        nota50 = (troco / 50)
        nota20 = (troco / 20)
        nota10 = (troco / 10)
        nota5 = (troco / 5)
        moeda1 = (troco / 5)
        if nota50 == 0:
            print(f"O troco será dado em {nota50} de R$50")
