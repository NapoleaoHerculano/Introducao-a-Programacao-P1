import bibliotecaCorreios

vl_final = 0
quant_sedex = 0

exe=int(input("Quantidade de entregas:"))
for i in range(exe):
    tipodeitem=str.upper(input("Tipo de Item-(Pacote ou Documento):"))
    peso=float(input("Peso(em gramas):"))
    embalagem=str.lower(input("Tamanho da embalagem-(Pequena,Média,Grande):"))
    tipodeentrega=str.lower(input("Tipo de entrega-(Normal,Sedex,Sedex 10):"))

    if tipodeentrega == "sedex" or tipodeentrega == "sedex 10":
        quant_sedex += 1
        
    vl_item = bibliotecaCorreios.calculaCustoItem(tipodeitem,peso)
    vl_embalagem = bibliotecaCorreios.calculaCustoEmbalagem(embalagem)
    vl_entrega = bibliotecaCorreios.calculaCustoEntrega(tipodeentrega)

    total = vl_item+vl_embalagem+vl_entrega

vl_final += total

print("Total arrecadado:R$:%.2f" %vl_final)
print("Pacotes enviados por SEDEX ou SEDEX 10:", quant_sedex)
