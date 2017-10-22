#Exercício Slide Comando Condicional - Slide 19

salario=float(input("Digite seu salário:"))

if salario>=1000:
    imposto=(salario*0.17)
else:
    imposto=(salario*0.08)
print("Valor do Imposto R$:%.2f" % imposto)
