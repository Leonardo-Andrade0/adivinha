import random

numero_secreto = random.randint(1, 100)

print("🎯 Jogo de Adivinhar o Número")
print("Pensei em um número entre 1 a 100.")

palpite = int(input("Qual é o seu palpite? "))

if palpite == numero_secreto:
    print("Acertou! 🎉")
else:
    print(f"Errou! O número era {numero_secreto}.")