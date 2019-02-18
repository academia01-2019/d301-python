# 2) Faça um programa que receba quatro número e mostre
# a média entre os quatro.

n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
n3 = float(input("Número 3: "))
n4 = float(input("Número 4: "))

soma = n1+n2+n3+n4
media = soma/4

media_direto = (n1+n2+n3+n4)/4

print("A média é: "+str(media))
print(f"A média é: {media_direto}")
