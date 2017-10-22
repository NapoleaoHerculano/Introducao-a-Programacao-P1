cont = 0

numero1=int(input("Primeiro Número:"))
numero2=int(input("Segundo Número:"))

if numero1 > numero2:
    for i in range(numero2+1,numero1):
        if i %4 == 0:
            cont += 1
else:
    for i in range(numero1+1,numero2):
        if i %4 == 0:
            cont += 1

print("Múltiplos de 4: %.0f" %cont)
