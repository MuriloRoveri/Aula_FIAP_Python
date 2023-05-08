import re 
erro = ""
try :
    print("Digite seu nome")
    nome = input()
    if re.search("\d", nome):
        erro = "Nomes não podem conter número"
        raise ValueError
    print("Digite seu CEP (somente dígitos)")
    cep = input()
    if not re.search("\d{8}",cep) or len(cep) > 8:
        erro = "CEP deve conter 8 dígitos"
        raise ValueError
    print(f"Nome: {nome}\nCEP: {cep}")
except ValueError:
    print(erro)
finally:
    print("Fim de programa!")