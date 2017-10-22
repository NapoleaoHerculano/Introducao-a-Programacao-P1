#variáveis móvel
marfim = 0
branco = 0
movel = 0
#variáveis eletrodoméstico
brastemp = 0
electrolux = 0
#variáveis de cálculo
quant_eletro = 0
quant = 0
media = 0

#Entradas
exe=int(input("Digite a quantidade de vendas:"))
for i in range(exe):
    tipo_produto = str.lower(input("Tipo de produto:"))

    if tipo_produto == "móvel":
        cor=str.lower(input("Cor:"))
        if cor == "marfim":
            marfim += 1
            movel += 1
        elif cor == "branco":
            branco += 1
            movel += 1
        else:
            print("Cor inválida!")
   
    elif tipo_produto == "eletrodoméstico":
        marca = str.lower(input("Marca:"))
        if marca == "brastemp":
            brastemp += 1
            quant_eletro += 1
        elif marca == "electrolux":
            electrolux += 1
            quant_eletro += 1
        else:
            print("Marca inválida!")
            
    elif tipo_produto == "decoração":
        descricao=str.lower(input("Descrição:"))
        preço = int(input("Preço:"))
        media += preço
        quant += 1

    else:
        print("Tipo de produto inválido!")
        
#Condicionais        

#Móveis
if movel > 0:
    p_marfim = (marfim/movel)*100
    p_branco = (branco/movel)*100
    print("Percentuais: %.0f Marfim, %.0f Branco" %(p_marfim, p_branco))
else:
    print("Nenhum móvel foi vendido")
        
#Eletrodomésticos
if quant_eletro > 0:
    if brastemp > electrolux:
        print("Marca mais vendida:Brastemp")
    elif electrolux > brastemp:
        print("Marca mais vendida:Electrolux")       
    else:
         print("As duas marcas foram igualmente vendidas")
else:
    print("Nenhum eletrodoméstico vendido")

#Decoração
if quant > 0:
    dec_media = media/quant
    print("Preço médio da decoração R$:%.2f" %dec_media)
else:
    print("Nenhum objeto de decoração vendido")
