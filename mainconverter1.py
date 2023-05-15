def converter():
    liste_input = input()
    liste = liste_input.split()
    index = len(liste) - 1
    liste2 = []
    while index >= 0:
        liste2.append(liste[index])
        index -= 1
    print(liste2)

converter()