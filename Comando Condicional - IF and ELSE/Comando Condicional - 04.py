#4. Escreva um programa que receba como entrada um número e
#exiba mensagens informando:

#Se ele é ímpar
#Se ele é múltiplo de 3
#Se ele é divisor de 102

numero=int(input("Digite um número:"))

if numero % 2 == 0:
    print ("Número não é ímpar")
else:
    print ("Número é ímpar")

if numero % 3 == 0:
    print("Número é múltiplo de 3")
else:
    print("Número não é multiplo de 3")

if 102 % numero == 0:
    print("Número é divisor de 102")
else:
    print("Número não é divisor de 102")
    
