#3. Escreva um programa que receba como entrada três números e
#exiba uma mensagem informando qual é o maior deles.
#(Dica: desconsidere a entrada de números iguais)

numeroA=int(input("Digite o valor de A:"))
numeroB=int(input("Digite o valor de B:"))
numeroC=int(input("Digite o valor de C:"))

if numeroA > numeroB > numeroC:
    print("O maior número é:", numeroA)
elif numeroB > numeroC:
    print("O maior número é:", numeroB)
else:
    print("O maior número é:", numeroC)
    
