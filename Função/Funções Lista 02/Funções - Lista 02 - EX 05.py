import bibliotecaExercicio2

multiplosde4 = 0
soma_div_300 = 0

exe=int(input("Quantidade de números:"))
for i in range(exe):
    num=int(input("Insira um número:"))
    funcao = bibliotecaExercicio2.testaMultiplo4(num)
    multiplosde4 += funcao

    div_300 = bibliotecaExercicio2.testaDivisor(300,num)
    if div_300 == True:
        soma_div_300 += num
    
print("Múltiplos de 4:", multiplosde4)
print("Soma dos Divisores de 300:", soma_div_300)
    
