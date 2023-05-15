def flatten_func(liste):
    duz_liste = []
    for eleman in liste:
        if isinstance(eleman, list):
            duz_liste.extend(flatten_func(eleman))
        else:
            duz_liste.append(eleman)
    return duz_liste
liste = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
flatten_list = flatten_func(liste)
print(flatten_list)
