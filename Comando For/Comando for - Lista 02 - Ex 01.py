#1. Rafaela tem uma loja de antiguidades e decidiu avaliar quanto vale
#o seu estoque. Escreva um programa que receba como entrada a quantidade
#de peças no estoque, e posteriormente, receba a descrição, o valor e o ano
#de cada item do estoque e exiba: 

descricao_valioso = 0
ano_valioso = 0
obj_valioso = 0
obj_antigo = 0
soma = 0

quant=int(input("Digite a quantidade de peças no estoque:"))
for i in range(quant):
    descricao = str(input("Descrição do produto:"))
    valor = int(input("Valor do produto R$:"))
    ano = int(input("Ano de ""fabricação:"))
   
    if ano <= 1827:    
      obj_antigo += 1

    if valor > obj_valioso:
        obj_valioso = descricao
        ano_valioso = ano
        descricao_valioso = descricao

    obj_valioso = valor
        
   
    soma += valor
    media = soma/quant


print("Itens produzidos antes de 1827:", obj_antigo)
print("Valor médio dos itens R$:%.2f" %media)
print("Dados do objeto mais valioso:%s,%d" %(descricao_valioso,ano_valioso))
    
