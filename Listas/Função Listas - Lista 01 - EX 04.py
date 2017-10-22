lista = []
soma = []

for i in range(5):
    num=int(input())
    lista.append(num)
for i in range(4):
    funcao=((lista[0]+lista[1]),(lista[1])+lista[2])
    soma.append(funcao)
print(lista)
print(soma)
