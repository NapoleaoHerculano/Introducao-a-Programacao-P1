valor = 0
seco = 0
total = 0

exe= int(input("Quantos pedidos deseja verificar:"))
for i in range(1,exe+1):
    tipo=str.lower(input("Digite o tipo de cobrança - Peça ou Quilo:"))

    if tipo == "peça":
        quant=int(input("Digite a quantidade de peças:"))
        valor = 7 * quant
        
    elif tipo == "quilo":
        quilos = int(input("Quilos:"))
        valor = 5 * quilos

    lavagem=str.lower(input("Deseja lavagem a seco?:"))


    if lavagem == "sim":
        valor = valor + 3.50
        seco += 1
    else:
        valor = valor

    total += valor
    print("Valor do pedido %.0f : %5.2f" %(i,valor))


print("Total arrecadado R$: %.2f" %total)
print("Quantidade de lavagens a seco: %.0f" %seco)
    


