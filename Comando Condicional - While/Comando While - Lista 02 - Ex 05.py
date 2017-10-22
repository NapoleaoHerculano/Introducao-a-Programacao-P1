#5. O Ministério da Saúde deseja vacinar contra o sarampo todas as crianças de 3 a 6 anos.
#Escreva um programa para ser usado em uma escola que receba como entrada a idade
#de várias crianças até que o usuário não deseje mais informar dados, e calcule e
#exiba a quantidade total de vacinas aplicadas.

off = 0
vacinas = 0

print("Para parar o programa digite - 100")

while (off != 100):
    idade = int(input("Digite a idade da criança:"))
    off = idade

    if idade >= 3 and idade <= 6:
        vacinas += 1

print("Quantidade total de vacinas aplicadas: %.0f" %vacinas)
        
