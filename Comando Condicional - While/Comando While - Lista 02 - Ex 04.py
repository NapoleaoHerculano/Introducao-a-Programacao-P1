#4. Escreva um programa que receba como entrada vários números, até que seja
#informado o valor 100, e exiba a média dos números pares. (Dica: a média dos
#números é calculada dividindo-se sua soma pela quantidade de números. Porém,
#como não é possível dividir por zero, se houver dúvida sobre a quantidade, é
#preciso testar antes de fazer o cálculo).

cont = 0
soma = 0
numero = 0
pares = 0


while(numero != 100):
    numero=int(input("Digite um valor:"))
    cont += 1

    if numero %2 == 0 and numero != 100:
        soma += numero
        pares += 1
    else:
        pares - 1

if pares == 0:
    print("Não foram lidos números pares!")
    exit(0)
    
media = soma/pares

print("Média:%.0f" % media)
 
 
