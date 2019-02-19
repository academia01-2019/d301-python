# 5) Faça um programa que receba quantos números terá no cálculo da média
# e retorne a média deles. 

quantidade = int(input("Digite quantos números terá no cálculo"))

soma = 0

#for i in range(inicio, parada, passo)
# - o inicio é o valor de inicio do i
# - parada é até onde o valor vai sem incluir ele 
# - passo é de quanto em quanto nosso valor vai mudar(ex: de um em um, de dois em dois, de menos um em menos um...) 

#se vc passar só um valor no range() ele passa de um em um partindo do zero
#se vc passar dois valores ele passa de um em um comçando no primeiro número e parando no segundo
#se vc passar três valores ele passa de acordo com o ultimo numero começando do primeiro e parando no segundo

for i in range(quantidade):
    num = float(input("Digite o número: "))
    soma = soma + num

media = soma/quantidade
print("A média será: "+str(media))
