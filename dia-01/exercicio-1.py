# 1) Faça um programa que receba dois números e mostre:
#     - A soma
#     - A subtração 
#     - A multiplicação
#     - E a divisão entre os dois


#input() recebe um valor digitado pelo usuario no console
#float() transforma em numero decimal a o valor digitado no input

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

soma = n1+n2
print("A soma dos números é "+str(soma)) #str transforma a variavel soma que é um numero decimal em texto
#print() imprime um valor no terminal

sub = n1-n2
print("A substração dos números é "+str(sub))

mult = n1*n2
print("A multiplicação dos números é %f" % mult) #"texto %f" % mult subistitui o valor de %f por %

div = n1/n2
print(f"A divisão dos números é {div}") #f"texto {variavel}" concatena a string com a variavel div, como se fosse o template string no js