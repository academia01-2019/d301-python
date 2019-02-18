# 5) Faça um programa que receba quantos números terá no cálculo da média
# e retorne a média deles. 

quantidade = int(input("Digite quantos números terá no cálculo"))

soma = 0

for i in range(quantidade):
    num = float(input("Digite o número: "))
    soma = soma + num

media = soma/quantidade
print("A média será: "+str(media))
