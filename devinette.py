import random

def choisir_nombre():
    minimum = input("Entre la nombre minimale (0 par défaut) : ")
    maximum = input("Entre la nombre maximale (100 par défaut) : ")

    if minimum == "":
        minimum = 0
    else:
        minimum = int(minimum)

    if maximum == "":
        maximum = 100
    else:
        maximum = int(maximum)

    return minimum, maximum


minimum, maximum = choisir_nombre()

nombre_secret = random.randint(minimum, maximum)
essais = 0

print(f"J'ai choisi un nombre entre {minimum} et {maximum}")

while True:
    essai = int(input("Entre ton essai : "))
    essais += 1

    if essai < nombre_secret:
        print("C'est plus grand !")

    elif essai > nombre_secret:
        print("C'est plus petit !")

    else:
        print("Bravo !")
        print(f"Tu as réussi en {essais} essais.")
        break