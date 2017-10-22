lista = []
notas_altas = 0

for i in range(5):
    notas=float(input())
    lista.append(notas)
    if notas > 8:
        notas_altas += 1
print(notas_altas)

    
    
