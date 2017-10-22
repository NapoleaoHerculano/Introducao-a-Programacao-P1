#Exercício Slide Comando Condicional - Slide 21

idade=int(input("Digite sua idade:"))

if idade <= 5:
    ingresso = 10
elif idade >= 60:
    ingresso = 15
else:
    ingresso = 25

print ("Valor a ser pago RS:%.2f" % ingresso)
