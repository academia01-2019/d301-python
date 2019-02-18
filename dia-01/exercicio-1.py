# 1) Faça um programa que receba dois números e mostre:
#     - A soma
#     - A subtração 
#     - A multiplicação
#     - E a divisão entre os dois

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

soma = n1+n2
print("A soma dos números é "+str(soma))

sub = n1-n2
print("A substração dos números é "+str(sub))

mult = n1*n2
print("A multiplicação dos números é %f" % mult)

div = n1/n2
print(f"A divisão dos números é {div}")