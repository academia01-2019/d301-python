# 3) Faça um programa que receba uma temperatura em Celcius e
# retorne ela em Fahrenheit. A fórmula de conversão é:
#                 F = (C * 9/5) + 32

celcius = float(input("Digite a temperatura em Celcius: "))

fah = (celcius * (9/5)) + 32

print(f"A temperatura {celcius}C em fahrenheit é: {fah}F!")