#A partir de la liste L=[1234, 17, 42, 25, 78, 17, 85]. Réaliser un script qui affiche la liste, compte le nombre
#d’occurrence de 17, ajoute en dernière position de la liste la somme des termes de la liste, donne le nombre
#d’éléments de la liste, supprime le terme 25 et renverse l’ordre de la liste.

L = [1234, 17, 42, 25, 78, 17, 85]


# Affichage de ma Liste
for mylist in L:
    print(mylist)
    

# compte le nombre d’occurrence de 17
count17 = L.count(17)
print("Le nombre 17 apparait : {} fois".format(count17))


# Somme des termes de la liste en dernière position de la liste.
somme = sum(L)
print("Voici la somme des termes de la liste : {}".format(somme))

# Append pour mettre à la fin de ma liste la somme des éléments de ma liste, une nouvelle boucle pour la preuve que cela marche.
L.append(somme)
for mylist in L:
    print(mylist)


# Donne le nombre d'élement de la liste
countL = len(L)
print("Il y a : {} éléments dans la liste".format(countL))


# Supprime le terme 25
deleteElementL = L.remove(25)
# Preuve que le 25 y est plus :
print("Preuve que le 25 y est plus :")
for banned25 in L:
    print(banned25)


# renverse l’ordre de la liste
reverseL = L.reverse()
# Preuve que la liste est reverse : 
print("Preuve que la liste est reverse :")
for mylistReverse in L:
    print(mylistReverse)

