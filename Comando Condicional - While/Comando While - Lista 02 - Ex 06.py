#6. Escreva um programa que receba como entrada a quantidade de filhos dos vários
#funcionários de uma empresa, até que seja informada uma quantidade negativa,
#e exiba a quantidade média de filhos do grupo. (Dica: a média pode ser obtida
#dividindo-se a soma dos números pela quantidade deles).

cont=-1
soma=1
filhos=0

print ("Caso deseje parar o programa e realizar o calculo --- Digite: -1")

while (filhos >= 0):
    filhos=int(input("Digite a quantidade de filhos:"))
    cont = cont + 1
    soma = soma + filhos

if (filhos == -1):
    media = (soma)/ cont

print ("A quantidade média de filhos do grupo é de:%5.2f filho(s) por funcionário." % media)
