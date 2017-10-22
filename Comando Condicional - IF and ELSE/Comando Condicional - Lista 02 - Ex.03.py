onibus=42
vl_onibus=350

van=20
vl_van=200

quant_bus=0
quant_van=0

quant_pessoas=int(input("Digite a quantidade de pessoas:"))

if quant_pessoas <= 20:
    vl_final = vl_van/quant_pessoas
    quant_van += 1
    print(quant_van)

if quant_pessoas <= 42:
    vl_final = vl_onibus/quant_pessoas
    quant_bus += 1
    print(quant_bus)

elif quant_pessoas > 42:
    quant_bus += 1
    quant_van += 1
    print(quant_van)
    print(quant_bus)
    vl_final = (vl_onibus + vl_van)/quant_pessoas

print("R$ %.2f" % vl_final)
