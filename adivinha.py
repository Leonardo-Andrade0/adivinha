import random

numero_secreto = random.randint(1, 100)

print("🎯 Jogo de Adivinhar o Número")
print("Pensei em um número entre 1 e 100.")

acertou = False

while not acertou:
    palpite = int(input("Qual é o seu palpite? "))

    if palpite == numero_secreto:
        print("Acertou! 🎉")
        acertou = True
    else:
        print("Errou, tente de novo!")