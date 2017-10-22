gasolina=2.53
etanol=2.09
diesel=1.92

tipo_combustivel=str.lower(input("Digite o tipo de combustível:"))
valor=int(input("Digite o valor a ser abastecido R$:"))

if tipo_combustivel == "gasolina":
    litros=valor/gasolina
elif tipo_combustivel == "etanol":
    litros=valor/etanol
elif tipo_combustivel == "diesel":
    litros=valor/diesel
else:
    print("Tipo de combustível inválido!")

print("Litros:%.2f" %litros)

if litros >= 30:
    print("Você ganhou uma troca de óleo")
else:
    print("Você não ganhou uma troca de óleo")

