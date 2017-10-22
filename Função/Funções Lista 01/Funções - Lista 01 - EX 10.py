import bibliotecaCorreios

tipodeitem=str.upper(input("Tipo de Item:"))
peso=float(input("Peso(em gramas):"))
embalagem=str.lower(input("Tamanho da embalagem:"))
tipodeentrega=str.lower(input("Tipo de entrega:"))

vl_item = bibliotecaCorreios.calculaCustoItem(tipodeitem,peso)
vl_embalagem = bibliotecaCorreios.calculaCustoEmbalagem(embalagem)
vl_entrega = bibliotecaCorreios.calculaCustoEntrega(tipodeentrega)

vl_final = vl_item+vl_embalagem+vl_entrega

print("Valor da postagem R$:%.2f" %vl_final)
