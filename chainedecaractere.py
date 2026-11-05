def count_word(texte):
    return len(texte.split())


phrase = input("Entrez une phrase : ")

nombre_mots = count_word(phrase)

print(f"Nombre de mots : {nombre_mots}")