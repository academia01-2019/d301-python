# 4) Faça um programa que receba dois inputs, uma palavra/frase
# e uma letra. O programa deve retornar quantas vezes a letra apareceu
# na palavra/frase. Dica: contagem de valores .count('valor')

# 1- Jeito fácil
frase = input("Digite uma frase ou palavra: ")
letra = input("Digite uma letra: ")

contagem = frase.count(letra)
print(f"A letra {letra} aparece {contagem} vezes na palavra {frase}")

# 2- Jeito hardcore
frase = input("Digite uma frase ou palavra: ")
letra = input("Digite uma letra: ")

contador = 0
for i in frase:
    if i is letra:
        contador = contador + 1
    
print(f"A letra {letra} aparece {contador} vezes na palavra {frase}")

# 3- Jeito "completo"
frase = input("Digite uma frase ou palavra: ")
letra = input("Digite uma letra: ")

contagem = frase.count(letra)
if contagem == 0:
    print(f"A letra {letra} não aparece na palavra!")
else:
    print(f"A letra {letra} aparece {contagem} vezes na palavra {frase}")
