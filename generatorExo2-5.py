# 2.5. Ecrire un script générant un nombre aléatoire compris entre 1 et 9 inclus. Demander à l’utilisateur de trouver ce
# nombre, en retour programme indiquera too low, too high, ou exactly right.
import random

valueGenerate = random.randint(1,9)
valueUser = int(input("Entrer un nombre : "))

while not(valueUser == valueGenerate):
    if valueUser > valueGenerate:
        print("too high")
    else:
        print("too low")
    valueUser = int(input("Entrer un nombre : "))

print("exactly right, c'était : {}".format(valueUser))
