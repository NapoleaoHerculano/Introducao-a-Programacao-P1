vip = 350
cadeira = 200
arquibancada = 100
conveniencia = 0.05


setor=str.lower(input("Digite o setor de sua escolha:"))
ingresso=str.lower(input("Digite o tipo de entrada (Meia ou Inteira):"))

if setor == "platéia vip":
    valor = vip
    if ingresso == "meia":
        print("Tipo de ingresso inválido!")
        exit(0)
elif setor == "cadeira":
    valor = cadeira
elif setor == "arquibancada":
    valor = arquibancada
else:
    print("Opção Inválida!")
    exit(0)

if ingresso == "meia":
    vl_final = valor/2+(valor*conveniencia)
elif ingresso == "inteira":
    vl_final = valor+(valor*conveniencia)
else:
    print("Tipo de ingresso inválido!")

print("Valor do ingresso R$:%.2f" %vl_final) 
