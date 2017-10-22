import bibliotecaExercicio2

maior = 0

exe=int(input("Quantidade de números:"))
for i in range(exe):
    num=int(input("Digite um valor:"))
    funcao = bibliotecaExercicio2.calculaMaior(num,maior)
    maior = funcao
    
print(maior)
