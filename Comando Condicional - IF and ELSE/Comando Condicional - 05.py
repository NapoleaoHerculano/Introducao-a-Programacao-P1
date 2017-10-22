#5. Natália abriu uma loja de bijuterias recentemente e as vendas vão muito bem.
#Pensando em atrair uma clientela ainda maior, ela deseja oferecer um desconto de
#10% para os clientes que gastarem R$ 100 ou mais e pagarem em dinheiro.
#Escreva um programa que receba como entrada o valor do produto comprado e a forma de pagamento escolhida (dinheiro ou cheque),
#calcule o desconto devido (caso necessário), e exiba o valor final a ser pago.

preço=float(input("Digite o valor do produto - R$:"))
pagamento=str.lower(input("Digite a forma de pagamento (Dinheiro ou Cheque):"))

if pagamento == "dinheiro":
    if preço >= 100:
        desconto = preço - (preço*0.10)
    else:
        desconto = preço
elif pagamento == "cheque":
    desconto = preço
else:
    print("Forma de pagamento inválida")

print ("Valor a ser pago R$:%.2f" % desconto)
