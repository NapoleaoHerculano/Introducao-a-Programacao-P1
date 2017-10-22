#6. Passados seis meses, a loja de Natália teve um crescimento surpreendente
#e agora ela vai aceitar pagamentos também com cartão. O cliente poderá escolher
#entre as funções débito e crédito do cartão, e ainda parcelar sua compra em até 3
#vezes na opção crédito. Modifique o programa anterior para que as novas formas
#de pagamento sejam consideradas e, além do valor final a ser pago, seja exibido o
#valor de cada parcela nas compras com cartão de crédito. 
 

preço=float(input("Digite o valor do produto - R$:"))
pagamento=str.lower(input("Digite a forma de pagamento (Dinheiro/Cheque/Cartão):"))

if pagamento == "dinheiro":
    if preço >= 100:
        desconto = preço - (preço*0.10)
    else:
        desconto = preço
if pagamento == "cheque":
    desconto = preço
if pagamento == "cartão":
    função = str.lower(input("Débito ou Crédito?:"))
    if função == "crédito":
        parcelas = int(input("Deseja dividir em quantas vezes?:"))
        if parcelas >3:
            print("Quantidade de parcelas inválida.")  
        vl_parcelas = preço/parcelas
        print("Valor a ser pago R$:%.2f" % preço)
        print("Em %d parcelas" % parcelas)
        print("De R$:%.2f" % vl_parcelas)
    else:
        print("Valor a ser pago R$:%.2f" % preço)
    

print ("Valor a ser pago R$:%.2f" % desconto)

